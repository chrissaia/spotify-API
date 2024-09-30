import matplotlib.pyplot as plt
from io import BytesIO
import base64

# function to plot genre distribution
def plot_genre_distribution(genre_data):
    genres = list(genre_data.keys())
    counts = list(genre_data.values())

    plt.figure(figsize=(10, 6))
    plt.bar(genres, counts)
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('genres')
    plt.ylabel('count')
    plt.title('genre distribution in playlist')
    plt.tight_layout()

    # save plot to BytesIO and encode as base64
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return img_base64
