import tkinter as tk
memo=[0 if i==0 else 1 if i == 1 else None for i in range(100) ]
def fibo_memoization(n:int)-> int:

    '''
    fibonacci function by recursion with memoization
    :param n: integer number
    :return: integer number
    '''
    global memo
    if memo[n] is not None:
        return memo[n]

    result = fibo_memoization(n-1)+fibo_memoization(n-2)
    memo[n]=result
    return result
def process_fibonacci():
    number = int(en_input_number.get())#input
    # lbl_display_fibonacci_result.config(text=f"{number+1}") #display
    lbl_display_fibonacci_result.config(text=f"fibonacci({number})={fibo_memoization(number)}")  # display
#   print(number+1) 할때는 console창에 올라옴


if __name__=="__main__":
    w=tk.Tk() #create window object
    w.title("Fibonacci")
    w.geometry("250x100")
    #create widget
    lbl_display_fibonacci_result=tk.Label(w,text="Fibonacci by memoization")
    en_input_number=tk.Entry(w)#입력상자 만들기
    btn_click=tk.Button(w,text="Click",command=process_fibonacci) #여기까진 안올라갔음
    #bind function

    #layout
    lbl_display_fibonacci_result.pack()
    en_input_number.pack(fill="x")
    btn_click.pack(fill="x")
    en_input_number.focus()

    w.mainloop()


# n=int(input("Int number: ")) # Input box
# print(f"fibonacci({n})={fibo_memoization(n)}") # Label


