class Seq:

    def __init__(self, strbases):

        print("You have created a new sequence")

        self.strbases = strbases

    def len(self):
        len_seq = len(self.strbases)

        return len_seq

    def complement(self):

        seqcomp = ""

        for n in self.strbases:
            if n == "A":
                seqcomp += "T"
            elif n == "T":
                seqcomp += "A"
            elif n == "C":
                seqcomp += "G"
            elif n == "G":
                seqcomp += "C"
        return seqcomp

    def reverse(self):

        seqrev = self.strbases[::-1]

        return seqrev

    def count(self):

        count_a = 0
        count_t = 0
        count_c = 0
        count_g = 0

        for n in self.strbases:

            if n == "A":

                count_a += 1

            elif n == "T":

                count_t += 1

            elif n == "G":

                count_g += 1

            elif n == "C":

                count_c += 1

        return ["A: ", count_a, "T", count_t, "C", count_c, "G", count_g]

    def perc(self):

        len_seq = len(self.strbases)
        count_a = 0
        count_t = 0
        count_c = 0
        count_g = 0

        for i in self.strbases:
            if i == "A":
                count_a += 1
            elif i == "T":
                count_t += 1
            elif i == "G":
                count_g += 1
            elif i == "C":
                count_c += 1

        if len_seq > 0:
            per_a = round(100.0 * count_a / len_seq, 1)
            per_t = round(100.0 * count_t / len_seq, 1)
            per_g = round(100.0 * count_g / len_seq, 1)
            per_c = round(100.0 * count_c / len_seq, 1)
        else:
            per_a = 0
            per_t = 0
            per_g = 0
            per_c = 0

        return per_a, per_c, per_g, per_t
