from model.model_usage import predict_fashion_item

result = predict_fashion_item('image.jpg')
print(f"Color: {result['color']}")
print(f"Product: {result['product']}")
