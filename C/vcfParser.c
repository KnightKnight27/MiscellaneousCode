#include <stdio.h> 


int main(int argc, char** argv)
{
    if (argc != 2)
    {
        printf("\n");
        printf("Usage:\n");
        printf("vcfParser fileName:\n");
        printf("\n");
        return 1;
    }

    char* vcf_file_name = argv[1];
    printf("Parsing VCF file %s\n", vcf_file_name);
    return 0;
}
