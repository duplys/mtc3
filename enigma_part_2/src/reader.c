#include <stdlib.h>
#include <stdio.h>
#include <gsl/gsl_statistics.h>

static double
english_frequencies[26] = {12.702, 9.056, 8.167, 7.507, 6.9662, 6.749, 6.327, 6.094, 5.987, 4.253, 4.025, 2.782, 2.758, 2.406, 2.360, 2.228, 2.015, 1.974, 1.929, 1.492, 0.978, 0.772, 0.153, 0.150, 0.095, 0.074};


int compare_doubles (const void *a, const void *b) {
	const double *da = (const double *) a;
	const double *db = (const double *) b;
	return (*da < *db) - (*da > *db);
}



int main(int argc, char ** argv) {

  FILE * fp, * fresult;
  char * pt;
  unsigned char alphabet[26] = {65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90};
  double frequencies[26] = {0};
	double correlation;
  int i,j;

  pt = malloc(800 * sizeof(char));
	
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
    for (j=0; j<789; j++) {
      if (pt[j] == alphabet[i])
				frequencies[i] = frequencies[i] + 1;
    }
  }

	qsort(frequencies, 26, sizeof(double), compare_doubles);
  
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
