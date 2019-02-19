from Seq import Seq

seq_1 = Seq(input("Introduce the first sequence: "))
seq_2 = Seq(input("Introduce the second sequence: "))
seq_3 = Seq(seq_1.complement())
seq_4 = Seq(seq_3.reverse())

str1 = seq_1.strbases
str2 = seq_2.strbases
str3 = seq_3.strbases
str4 = seq_4.strbases
len1 = seq_1.len()
len2 = seq_2.len()
len3 = seq_3.len()
len4 = seq_4.len()
count1 = seq_1.count()
count2 = seq_2.count()
count3 = seq_3.count()
count4 = seq_4.count()
per_1 = seq_1.perc()
per_2 = seq_2.perc()
per_3 = seq_3.perc()
per_4 = seq_4.perc()

print(str1, count1, per_1)
