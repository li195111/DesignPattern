from models import CircleFactory
    
if __name__ == "__main__":
    # To Create Product
    print (CircleFactory().create({'width':10, 'height':10, 'radius':10}))
    print (CircleFactory().create({'width':20, 'height':20, 'radius':20}))
    print (CircleFactory().create({'width':30, 'height':30, 'radius':30}))