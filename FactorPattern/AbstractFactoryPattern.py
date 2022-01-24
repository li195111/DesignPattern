from models import GraphicFactory, GraphType

if __name__ == "__main__":
    # To Create Factory
    print (GraphicFactory(GraphType.Circle).create())
    print (GraphicFactory(GraphType.Rectangle).create())
    print (GraphicFactory(GraphType.Triangle).create())
