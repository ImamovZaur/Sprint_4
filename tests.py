import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('book_name',['', 'x'*43])
    def test_add_new_book_with_len_0_and_43_book_not_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.add_new_book('Преступление и наказание')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_where_genre_in_genre_list(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Детективы')
        assert collector.books_genre['Преступление и наказание'] == 'Детективы'

    @pytest.mark.parametrize('name, genre',[
        ['Преступление и наказание', 'Детективы'],
        ['Мобильник','Ужасы']
    ])
    def test_get_book_genre_added_genre_from_list(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('name, genre', [
        ['Преступление и наказание', 'Детективы'],
        ['Мобильник', 'Ужасы']
    ])
    def test_get_books_with_specific_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert name in collector.get_books_with_specific_genre(genre)

    @pytest.mark.parametrize('name, genre', [
        ['Преступление и наказание', 'Детективы'],
        ['Мобильник', 'Ужасы']
    ])
    def test_get_books_genre_with_data_in_dict(self, name, genre):
        expected = {name: genre}
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_genre() == expected

    def test_get_books_for_children_genre_for_child(self):
        collector = BooksCollector()
        collector.add_new_book('Кот в сапогах')
        collector.set_book_genre('Кот в сапогах','Мультфильмы')
        assert 'Кот в сапогах' in collector.get_books_for_children()

    def test_get_books_for_children_genre_not_for_child(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание','Детективы')
        assert 'Преступление и наказание' not in collector.get_books_for_children()

    def test_add_book_in_favorites_book_isnt_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Мобильник')
        collector.add_book_in_favorites('Мобильник')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_book_already_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Мобильник')
        collector.add_book_in_favorites('Мобильник')
        collector.add_book_in_favorites('Мобильник')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_add_two_books_one_delete(self):
        collector = BooksCollector()
        collector.add_new_book('Мобильник')
        collector.add_new_book('Кот в сапогах')
        collector.add_book_in_favorites('Кот в сапогах')
        collector.add_book_in_favorites('Мобильник')
        collector.delete_book_from_favorites('Мобильник')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Кот в сапогах')
        collector.add_book_in_favorites('Кот в сапогах')
        assert 'Кот в сапогах' in collector.get_list_of_favorites_books()