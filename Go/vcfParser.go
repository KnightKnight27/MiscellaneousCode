package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)


type VCFRecord struct {
    contig string
    position int64
    id int64
    ref string
    alt string
    quality float64
    filters []string
    info map[string]string
    format string
    sample_data map[string]string
}


func create_vcf_record_from_string(input_string string) *VCFRecord {
    record := new(VCFRecord)

    for index,field := range strings.Split(input_string, "\t") {
        switch index {
            case 0:
                record.contig = field
            case 1:
                record.position, _ = strconv.ParseInt(field, 0, 64)
            case 2:
                record.id, _ = strconv.ParseInt(field, 0, 64)
            case 3:
                record.ref = field
            case 4:
                record.alt = field
            case 5:
                record.quality, _ = strconv.ParseFloat(field, 64)
        }
    }

    return record
}


func main() {
    input_file, error_code := os.Open("../testData/testData.vcf");

    if error_code == nil {
        input_file_reader := bufio.NewReader(input_file);

        for {
            line, _, error_code := input_file_reader.ReadLine()
            var vcf_line string = string(line); // Convert to text from binary
            fmt.Println(vcf_line);
            vcf_record := create_vcf_record_from_string(vcf_line)
            fmt.Printf("%+v\n", vcf_record)

            if error_code == io.EOF {
                break;
            }
        }
    }
}
