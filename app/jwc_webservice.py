from urllib import parse, request
from flask import Flask, jsonify
from flask import request
from app import app


@app.route('/books', methods=['GET', 'POST'])
def get_book():
    if request.method == 'POST':
        book_name = request.form.get('book_name')
        from app import book_main
        book = book_main
        content = book.get_content(book_name)
        list1 = book.get_booklist(content)
        list2 = book.get_booklistdetail(content)
        list4 = book.get_json(list1, list2)
        return jsonify(list4)


@app.route('/pagebooks', methods=['GET', 'POST'])
def get_pagebook():
    if request.method == 'POST':
        book_name = request.form.get('book_name')
        page_num = request.form.get('page_num')
        from app import book_main
        book = book_main
        content = book.get_numpage(book_name, page_num)
        list1 = book.get_booklist(content)
        list2 = book.get_booklistdetail(content)
        list4 = book.get_json(list1, list2)
        return jsonify(list4)


@app.route('/book_content', methods=['GET', 'POST'])
def get_book_content():
    if request.method == 'POST':
        book_index = request.form.get('book_index')
        from app import book_main
        book = book_main
        content = book.get_detail(book_index)
        return jsonify(content)


@app.route('/book_login', methods=['GET', 'POST'])
def get_booklogin():
    if request.method == 'POST':
        stnumber = request.form.get('stnumber')
        passwd = request.form.get('password')
        from app import clear_system
        book = clear_system.main()
        # print (book_index)
        content = book.cookie_login(stnumber, passwd)
        return jsonify(content)


@app.route('/new_book', methods=['GET', 'POST'])
def get_newbook():
    if request.method == 'POST':
        page = request.form.get('page')
        from app import new_book
        newbook = new_book.Main()
        content = newbook.get_newbook(page)
        return jsonify(content)


@app.route('/hot_book', methods=['GET', 'POST'])
def get_hot_book():
    if request.method == 'POST':
        from app import hot_book
        book = hot_book
        content = book.get_hotbook()
        return jsonify(content)


@app.route('/notice_list', methods=['GET', 'POST'])
def get_notice_list():
    if request.method == 'POST':
        from app import notice_list
        page = request.form.get('page')
        book = notice_list
        content = book.get_notice_list(page)
        return jsonify(content)


@app.route('/notice_content', methods=['GET', 'POST'])
def get_notice_content():
    if request.method == 'POST':
        from app import notice_content
        href = request.form.get('href')
        book = notice_content
        content = book.get_notice_content(href)
        return jsonify(content)


@app.route('/get_data', methods=['GET', 'POST'])  # 已废弃
def get_data():
    if request.method == 'POST':
        from app import data_sourse
        book = data_sourse.Main()
        content = book.get_data()
        return jsonify(content)


@app.route('/login', methods=['GET', 'POST'])
def get_login():
    if request.method == 'POST':
        code = request.form.get('code')
        from app import get_code
        book = get_code.main()
        content = book.get_code(code)
        return content


@app.route('/if_first', methods=['GET', 'POST'])
def get_first():
    if request.method == 'POST':
        code = request.form.get('user_id')
        from app import if_first
        book = if_first.main()
        content = book.if_first(code)
        return content


@app.route('/first_insert', methods=['GET', 'POST'])
def first_insert():
    if request.method == 'POST':
        from app import first_intel
        user_id = request.form.get('user_id')
        list = request.form.get('series_list')
        book = first_intel.main()
        content = book.insert_first(user_id, list)
        return content
