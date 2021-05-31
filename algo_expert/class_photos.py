def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    less_than = redShirtHeights[0] < blueShirtHeights[0]
    for i, height in enumerate(redShirtHeights):
        temp_less = height < blueShirtHeights[i]
        if temp_less != less_than or height == blueShirtHeights[i]:
            return False
    return True
