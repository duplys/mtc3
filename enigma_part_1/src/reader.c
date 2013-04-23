#include <stdlib.h>
#include <stdio.h>
#include <gsl/gsl_statistics.h>

static double
english_frequencies[26] = {8.167, 1.492, 2.782, 4.253, 12.70, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074};


int main(int argc, char ** argv) {

  FILE * fp, * fresult;
  char * pt;
  unsigned char alphabet[26] = {65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90};
  double frequencies[26] = {0};
	double correlation;
  int i,j;

  pt = malloc(512 * sizeof(char));
	
	if (argc != 2) {
		printf("Wrong number of arguments!\n");
		return 1;
	}
  
  fp = fopen(argv[1],"r");

  if(fscanf(fp, "%s\n", pt)) {
		#if 0
    printf("%s\n\n", pt);
		#endif
  }
  
  
  for (i=0; i<26; i++) {
    for (j=0; j<261; j++) {
      if (pt[j] == alphabet[i])
				frequencies[i] = frequencies[i] + 1;
    }
  }
  
  char res[50];
  sprintf(res, "output/frequencies_%d.dat", 0); 
  fresult = fopen(res, "w");
  
  for(i=0; i<26; i++) {
    fprintf(fresult, "%f\n", frequencies[i]);
  }

  fclose(fp);
  fclose(fresult);

	correlation = gsl_stats_correlation(english_frequencies, 1, frequencies, 1, 26);
	printf("%f\n", correlation);

	return 0;
}
