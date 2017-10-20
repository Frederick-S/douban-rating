from douban_rating.query import query

if __name__ == '__main__':
    ratings = query('flask')

    for rating in ratings:
        print(rating.title + ' ' + rating.rating)
