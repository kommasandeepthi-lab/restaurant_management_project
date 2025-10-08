def get_average_rating(reviews_queryset):
    try:
        if not reviews_queryset.exists():
            return 0.0

        total_rating = 0
        total_reviews = 0

        for review in reviews_queryset:
            rating = getattr(review, "rating", None)
            if rating is not None:
                total_rating += rating
                total_reviews += 1

            if total_reviews == 0:
                return 0.0

            average_rating = total_rating / total_reviews
            return round(float(average_rating), 2)

        except Exception:
            return 0.0