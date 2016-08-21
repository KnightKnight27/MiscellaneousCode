package main

import (
    "fmt"
    "io"
    "os"
    "bufio"
)


type vcf_record struct {
    contig string
    position int64
    ref string
    alt string
    quality float64
    filters []string
    info map[string]string
    format string
    sample_data map[string]string
}


func main() {
    input_file, error_code := os.Open("../testData/testData.vcf");

    if error_code == nil {
        input_file_reader := bufio.NewReader(input_file);

        for {
            line, _, error_code := input_file_reader.ReadLine()
            var vcf_line string = string(line); // Convert to text from binary
            fmt.Println(vcf_line);

            if error_code == io.EOF {
                break;
            }
        }
    }
}
