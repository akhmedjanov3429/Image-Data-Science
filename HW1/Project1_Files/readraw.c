// C Program to read and write raw images

#include <stdio.h>
#include <stdlib.h>

int main()

{
	// file pointer
	FILE *file;
	
	/* Program Variable */
	int BytesPerPixel=3;
	int Size = 128;
	
	/* image data array*/
	unsigned char Imagedata[128][128][3];
	unsigned char Outdata[128][128][3];

	/* Opening the input file */
	if (!(file = fopen("input_file_name.raw","rb")))
	{
		printf(" \n Cannot open file: ");
		exit(1);
	}
	fread(Imagedata, sizeof(unsigned char), Size*Size*BytesPerPixel, file);
	fclose(file);

	// Your image processing algorithm ....


	/* Opening the output file*/
	if (!(file=fopen("output_file_name.raw","wb")))
	 {
	   printf("\n Cannot open file: ");
	   exit(1);
	}

	/* Writing in the Output File */
	fwrite(Outdata, sizeof(unsigned char), Size*Size*BytesPerPixel, file);
	fclose(file);

	return 0;
}
