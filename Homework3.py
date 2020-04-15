student_score={1:70,2:80,3:90,4:100,5:90,6:50,7:60}

for i in range(1,8):
    if student_score[i] >= 80:
        print('학생 ' + str(i) + '번 학생은 합격입니다')
    else:
        print('학생 ' + str(i) + '번 학생은 불합격입니다')