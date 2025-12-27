def selection_sort(m_list):
    for i in range(len(m_list) -1):
        min_index = i
        for j in range(i+1, len(m_list)):
            if m_list[j] < m_list[min_index]:
                min_index = j            
            
        if i != min_index:
            temp = m_list[i]
            m_list[i] = m_list[min_index]
            m_list[min_index] = temp

    return m_list

my_list = [9, 8, 7, 6, 5, 4, 2, 1]

print(selection_sort(my_list))