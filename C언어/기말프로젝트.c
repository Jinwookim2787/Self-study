#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>
#include <wchar.h>
// 동적 메모리 할당한 이후에 free 꼭 넣어두기 !!!!!! 
// 구조체를 이용해서 교수님 정보와 조교의 신상정보를 넣기 위한 코드 
typedef struct{
		char name[20];
		char mail[30];
		int mobile;
		int office;
}PROFESSOR;

typedef struct {
		char name[20];
		char mail[20];
		int mobile;
}TA;

typedef struct{
	char type;
	union {
		PROFESSOR prof;
		TA ta;
		}u;
}PERSON; 
//구조체를 이용해서 학생들의 정보를 받아들이기위한 준비 
struct student {
	char name[20];
	char area[20], addres[20];//area는 특별시 및 시 단위의 행정구역을 의미하고 addres는 행정구역 구를 의미함.  
	char sf[20];// 이는 재학여부를 알기 위해서 넣는 것.  
	int age, num, re, gra;//re는 장학금 수혜 회수, num은 학번을 의미함, gra 는 학년을 의미함 .
	double cgpa;
};

int forbidden(int re, double cgpa, char *sf, char *name); //장학금 수여 대상을 확인하기 위해서 만들어짐 . 
int maxre(int a, int *ptr); 
int minre(int a, int *ptr2);
double sumCgpa(double *ptr3, double a);
double aveCgpa(double sum, double *ptr4);

int main()
{		//선언문 초반에  정리  
		FILE *ifp, *ofp;
		int i, j;
		struct student m[17];
		int max=0; 
		double sum = 0, ave;
		int min=100; 
		int *ptr;
		int *ptr2;
		double *ptr3, *ptr4;
		char h,l; //switch에서 정보 호출할 때 사용하려고 만든 변수  
		//포인터 이용하기 위해 초기화  
		ptr = &max;
		ptr2 = &min;
		ptr3 = &sum;
		ptr4 = &ave;
		PERSON data[3];
		
		data[0].type = 'p';
		strcpy(data[0].u.prof.name, "Tom");
		strcpy(data[0].u.prof.mail, "Topgunman@sogang.ac.kr");
		data[0].u.prof.mobile = 1012341234;
		data[0].u.prof.office = 301;
		
		data[1].type = 't';
		strcpy(data[1].u.prof.name, "Maira");
		strcpy(data[1].u.prof.mail, "CatholicMaria@sogang.ac.kr");
		data[1].u.prof.mobile = 1056785678;
		
		data[2].type = 't';
		strcpy(data[2].u.prof.name, "Kim");
		strcpy(data[2].u.prof.mail, "KoreanBoy@sogang.ac.kr");
		data[2].u.prof.mobile = 1078907890;
		
		//텍스트 파일에서 불러오기  
		int res; 	
		ifp = fopen("student.txt", "r");
		if(ifp==NULL){
			printf("input file open error!\n");
			return 1;
					}
		ofp=fopen("student information.txt", "wt");
		if(ofp==NULL){
			printf("output file open error!\n");
			return 1;}
		//텍스트 파일의 값을 구조체를 이용해서 정리하는 과정.  
		while(1) {
			res = fscanf(ifp, "%d%s%d%lf%d%s%d%s%s",&m[i].num, &m[i].name, &m[i].age, &m[i].cgpa, &m[i].gra, &m[i].sf, &m[i].re, &m[i].area, &m[i].addres);
			if(res==EOF) break;
			i++;
			if (i==17) break;
			}	
		//메모리에 입력값들을 넣어서 배열을 생성. 
		double **d = malloc(sizeof(double*)*17);
		for(i= 0; i<17; i++){
		d[i] = malloc(sizeof(double)*4);}
		for(i=0; i<17; i++)
		{d[i][0] = m[i].num; 
		 d[i][1] = m[i].gra;
		 d[i][2] = m[i].cgpa;	
		 d[i][3] = m[i].re;}
   	//어떤 케이스인지 선택할 수 있게 메뉴를 제공해준다.
	printf("원하시는 메뉴의 번호를 선택해주세요.\n1. 장학금관련 테이블\n2. 학생들 성적의 총합과 평균\n3. 장학금 최다및 최소 수여 학생의 정보\n4. 이번 학기 장학금 수여 학생\n"); 
	printf("\n메뉴를 입력해주세요: ");
	scanf(" %c", &h);
	printf("\n");
		
    switch(h){
	case '1':
    // 1번 메뉴  
	// 제일 처음 파일에서 읽은 값을 동적 메모리를 이용해서 만든 테이블에 넣어 보여준다.	
	printf("<1>\n");
	fprintf(ofp, "<1>\n");
	printf("이름  학번  \t  학년\t  성적\t 수여횟수\n");
	fprintf(ofp ,"이름  학번  \t  학년\t  성적\t 수여횟수\n");
	for(i=0; i<17; i++){ 
	    printf("%2s  ", m[i].name);
	    fprintf(ofp, "%2s  ", m[i].name);
	    for(j=0; j<4;j++){
	    	if(j==2) {
	    	fprintf(ofp,"%6.2f\t", d[i][j]);
			printf("%6.2f\t", d[i][j]);}
			else {
			fprintf(ofp,"%6.0f\t", d[i][j]);	
			printf("%6.0f\t", d[i][j]); }}
		printf("\n");
		fprintf(ofp, "\n");}
   	break;
   	
   case'2':
   //2번 메뉴  
    //학생들의 성적의 총합과 평균을 보여준다.
	printf("\n<2>");
	fprintf(ofp, "<2>"); 
	for(i=0; i<17; i++)
		sumCgpa(ptr3, m[i].cgpa);	
	aveCgpa(sum, ptr4); 
	printf("\n=> 학생들의 cgpa의 총합은  %.2f이며 평균은 %.2f입니다.\n ",sum, ave);
	fprintf(ofp ,"\n=> 학생들의 cgpa의 총합은  %.2f이며 평균은 %.2f입니다.\n ",sum, ave);
	break;
	
	case'3':
	//3번 메뉴  
	printf("\n<3>");
	fprintf(ofp, "<3>");
	//max값과 min값을 찾아내기 위한 코드  
	for(i=0; i<17; i++){
		maxre(m[i].re, ptr);
		minre(m[i].re, ptr2);}
	printf("\n");
	fprintf(ofp,"\n");
	// 위에서 구한 MAX값을 통해서 누가 최다 수여자인지 찾아내기 위한 프로그램임. -> 같은 수여 횟수를 갖더라도 값이 나오도록 설정함  
	for(i=0; i<17; i++){
		if(m[i].re<max) continue;
		else{
			printf("최대 장학금 수여 횟수는 %d회로 그 학생은 %s입니다.\n", max, m[i].name);
			printf("최다 장학금 수여자인 %s학생이 거주하는 지역은 %s, %s입니다", m[i].name, m[i].addres, m[i].area);
			fprintf(ofp, "최대 장학금 수여 횟수는 %d회로 그 학생은 %s입니다.\n\n", max, m[i].name );}
			fprintf(ofp, "최다 장학금 수여자인 %s학생이 거주하는 지역은 %s, %s입니다", m[i].name, m[i].addres, m[i].area);}
	printf("\n");
	printf("\n");
	fprintf(ofp,"\n");
	// 위에서 구한 MAX값을 통해서 누가 최다 수여자인지 찾아내기 위한 프로그램임. -> 같은 수여 횟수를 갖더라도 값이 나오도록 설정함		
	for(i=0; i<17; i++){
		if(m[i].re>min) continue;
		else{
			printf("가장 적은  장학금 수여 횟수는 %d회로 그 학생은 %s입니다.\n", min, m[i].name);
			printf("가장 적게 장학금을 탄  %s학생이 거주하는 지역은 %s, %s입니다\n", m[i].name, m[i].addres, m[i].area);
			fprintf(ofp, "가장 적은  장학금 수여 횟수는 %d회로 그 학생은 %s입니다.\n\n", min, m[i].name );}
			fprintf(ofp,"가장 적게 장학금을 탄  %s학생이 거주하는 지역은 %s, %s입니다\n", m[i].name, m[i].addres, m[i].area);}
	break;
	
	case '4':
	//4번 메뉴 누가 장학금을 탈 것인지.  
	printf("\n");
	printf("\n<4>\n");
	fprintf(ofp, "<4>\n");
	printf("==========<성적 장학대상>==============\n");
	fprintf(ofp, "===============<장학대상>====================\n");
	for(i=0; i<17; i++){
		if (forbidden(m[i].re, m[i].cgpa, m[i].sf , m[i].name)==1)
		fprintf(ofp, "%s: 성적 장학금 대상입니다.\n", m[i].name);
		}
		
	printf("=======================================\n\n");
	fprintf(ofp, "==========================================\n\n");
	break;
	}
	
		
	printf("\n성적관련 문의= g\n출결관련 문의= a\n과제점수관련 문의= r\n번호를 눌러주시면 담당자의 정보를 알려드리겠습니다.\n");	
	fprintf(ofp, "\n성적관련 문의= g\n출결관련 문의= a\n과제점수관련 문의= r\n문자를 입려해주시면 담당자의 정보를 알려드리겠습니다.\n");
	printf("\n문자를 입력해주세요: ");
	
	scanf(" %c", &l);
	switch(l){
		case 'g':
			printf("\n담당자 이름: %s\n", data[0].u.prof.name);
			printf("전화번호: %d\n", data[0].u.prof.mobile);
			printf("이메일 주소: %s\n", data[0].u.prof.mail);
			printf("교수님 사무실: %d호\n", data[0].u.prof.office);
			fprintf(ofp, "\n담당자 이름: %s\n", data[0].u.prof.name);
			fprintf(ofp, "전화번호: %d\n", data[0].u.prof.mobile);
			fprintf(ofp, "이메일 주소: %s\n", data[0].u.prof.mail);
			fprintf(ofp, "교수님 사무실: %d호\n", data[0].u.prof.office);
			break;
		case 'a':
			printf("\n담당자 이름: %s\n", data[1].u.ta.name);
			printf("전화번호: %d\n", data[1].u.ta.mobile);
			printf("이메일 주소: %s\n", data[1].u.ta.mail);
			fprintf(ofp,"\n담당자 이름: %s\n", data[1].u.ta.name);
			fprintf(ofp,"전화번호: %d\n", data[1].u.ta.mobile);
			fprintf(ofp,"이메일 주소: %s\n", data[1].u.ta.mail);
			break;
		case 'r':
			printf("\n담당자 이름: %s\n", data[2].u.ta.name);
			printf("전화번호: %d\n", data[2].u.ta.mobile);
			printf("이메일 주소: %s\n", data[2].u.ta.mail);
			fprintf(ofp, "\n담당자 이름: %s\n", data[2].u.ta.name);
			fprintf(ofp, "전화번호: %d\n", data[2].u.ta.mobile);
			fprintf(ofp, "이메일 주소: %s\n", data[2].u.ta.mail);
			break;
	}
	    for(i=0; i<17;++i){
		    free(d[i]);}
		
		free(d);
		fclose(ifp);
		fclose(ofp);
		return 0;}

// 장학금 수여 횟수, 휴학여부및 성적으로  장학금 수여 대상 여부 확인  
int forbidden(int re, double cgpa, char *sf, char *name)
{
	if(re<3&&cgpa>=3.65&& sf!= "휴학" ){
		printf("%s: ", name);	
		printf("장학금 수여 대상입니다.\n");
		return 1;}
	else
		return 0;}
//최대 장학금 수여 회수를 구하기 위한 함수  
int maxre(int a, int *ptr){
	if (a>*ptr) {
	*ptr = a;}}
//최소  장학금 수여 회수를 구하기 위한 함수  
int minre(int a, int *ptr2){
	if (a<*ptr2){
	*ptr2 = a;}}
// cgpa의 총합과 평균을 구하기 위한 함수
double sumCgpa(double *ptr3, double a){
	*ptr3 += a;
	return *ptr3;}
double aveCgpa(double sum, double *ptr4){
	*ptr4 = sum/17.0;
	return *ptr4;}
