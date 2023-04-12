class Stepik:
    def next_task(self):
        return "Следующее задание"

my_st = Stepik()

my_st.next_task(Stepik)

my_st.next_task()

Stepik.my_st.next_task()

Stepik.next_task(my_st)