#Latihan soal CDP Sinarmas 
#Membuat program menghitung karakter yang digunakan dalam kalimat

#using dict.get() to count each element of list
def main():
    print("========= Word Frequencies Counter =========")
    
    x = input("Input a Sentence: ")
    y = {}

    for i in x :
        y[i]=y.get(i, 0)+1
    
    #display the result in list 'y'
    print(str(y))

if __name__ == '__main__':
    main()
    
