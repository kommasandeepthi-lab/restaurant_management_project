def calculate_average_rating(reviews_queryset):
    try:
        total_reviews = reviews_queryset.count()
        if total_reviews == 0:
            return 0.0

        total_rating = sum(review.rating for review in reviews_queryset)
        return round(total_rating / total_reviews, 2)

    except Exception:
        return 0.0