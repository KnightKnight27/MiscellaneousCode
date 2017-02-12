#include <iostream>
#include <fstream>
#include <sstream>
#include <tuple>
#include <map>
#include <set>
#include <cmath>
#include <limits>

namespace oxam
{
    const int64_t INVALID_TIME_STAMP = -1;
    const char ORDER_INSERT = 'I';
    const char ORDER_ERASE = 'E';

    struct Order
    {
        const int64_t time_stamp;
        const int32_t id;
        const double price;
    };

    class OrderBook
    {
        public:
            void insert(const int64_t time_stamp, const int32_t id, const double price)
            {
                Order the_order = {time_stamp, id, price};
                m_orders.emplace(id, the_order);
                m_pricesAndIDs.insert(std::make_pair(price,id));
            }

            void erase(const int32_t id)
            {
                const auto& order = m_orders.at(id);
                m_pricesAndIDs.erase(std::make_pair(order.price,id));
                m_orders.erase(id);
            }

            double get_highest_price() const
            {
                if (m_orders.empty())
                {
                    return std::numeric_limits<double>::quiet_NaN();
                }
                else
                {
                    const auto& priceAndID = m_pricesAndIDs.rbegin();
                    return priceAndID->first;
                }
            }

        public:
            std::map<const int32_t, const Order> m_orders; // For O(lg(N)) look-up by ID
            std::set<std::pair<const double, const int32_t>> m_pricesAndIDs; // For O(lg(N)) look-up by price
    };


    class TimeWeightedHighPriceCalculator
    {
        public:
            void update(const int64_t time_stamp, const double price)
            {
                if (m_last_time_stamp == INVALID_TIME_STAMP) // First update
                {
                    m_last_time_stamp = time_stamp;
                    m_high_price = price;
                }
                else
                {
                    const auto time_since_last_update = time_stamp - m_last_time_stamp;

                    if (not std::isnan(m_high_price))
                    {
                        m_time_weighted_price_num += (m_high_price * time_since_last_update);
                        m_time_weighted_price_denom += time_since_last_update;
                    }

                    m_last_time_stamp = time_stamp;
                    m_high_price = price;
                }
            }

            double get_time_weighted_high_price() const {return m_time_weighted_price_num / m_time_weighted_price_denom;}

        private:
            int64_t m_last_time_stamp = INVALID_TIME_STAMP;
            double m_high_price = 0.0;
            double m_time_weighted_price_num = 0.0;
            double m_time_weighted_price_denom = 0.0;
    };
}


int main(int argc, char** argv)
{
    if (argc != 2)
    {
        std::cerr << "usage: compute_time_weighted_max_price <input file>" << std::endl;
        return EXIT_FAILURE;
    }

    const auto input_file_name = argv[1];
    std::ifstream input_file(input_file_name);
    std::string line;
    oxam::OrderBook order_book;
    oxam::TimeWeightedHighPriceCalculator calculator;

    while (std::getline(input_file, line))
    {
        std::stringstream line2(line);
        int64_t time_stamp;
        char operation;
        int32_t id;
        double price;

        line2 >> time_stamp >> operation >> id;

        if (operation == oxam::ORDER_INSERT)
        {
            line2 >> price;
            order_book.insert(time_stamp, id, price);
        }
        else if (operation == oxam::ORDER_ERASE)
        {
            order_book.erase(id);
        }

        const double highest_price = order_book.get_highest_price();
        calculator.update(time_stamp, highest_price);
    }

    std::cout << calculator.get_time_weighted_high_price() << std::endl;
    return EXIT_SUCCESS;
}
