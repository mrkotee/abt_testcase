def black_box(page: int):
    if page <= 7922400:
        return True
    else:
        return False


def calc_book_pages(max_pages):
    def get_page_num(page, max_pages, max_page=0, iteration=1):
        iteration += 1

        if black_box(page):
            if page > max_page:
                max_page = page
            next_num = int(page + max_pages / (2 ** iteration))
        else:
            next_num = int(page - max_pages / (2 ** iteration))

        if next_num == max_page:
            return max_page

        return get_page_num(next_num, max_pages, max_page, iteration)

    return get_page_num(max_pages/2, max_pages)


def main():
    """
    Вам дали книгу, конкретное количество страниц вам не сообщили,
    но оно точно не превышает 10 000 000.
    
    Вам необходимо вычислить номер последней страницы.
    Книгу открывать нельзя - вместо этого вам выдали черный ящик, чтобы слегка усложнить задачу.
    Черному ящику (функция black_box) можно сообщить предполагаемый номер последней страницы,
    а в ответ узнать, есть ли эта страница в книге.
    
    Уточнение:
        black_box возвращает True, если страница последняя
                  возвращает False, если страница не последняя.
    
    
    Важно: написать наиболее эффективный алгоритм (по числу итераций)
    """
    # тут явно нужен алгоритм
    max_pages = 10000000

    last_page_num = calc_book_pages(max_pages)

    print(last_page_num)


if __name__ == '__main__':
    main()

