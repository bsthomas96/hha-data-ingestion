{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyN6W7dqGWtO4LZ26+j0NpCO",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/bsthomas96/hha-data-ingestion/blob/main/python.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "J4IxOooR7vom"
      },
      "outputs": [],
      "source": [
        "import pandas as pd ## import pandas for general file types"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import json ## import json for json files"
      ],
      "metadata": {
        "id": "pgvOjcnED4DO"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import bs4 ## import bs4 for html files"
      ],
      "metadata": {
        "id": "8MhkVCbPD8gx"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import requests ## import requests for web requests"
      ],
      "metadata": {
        "id": "Vt8Tg2zlEAze"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import sqlalchemy ## import sqlalchemy for sql queries"
      ],
      "metadata": {
        "id": "sZrkwTHCEFBA"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from PIL import Image ## import pillow for image files"
      ],
      "metadata": {
        "id": "HCMEh5tdEM61"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google.cloud import bigquery ## import bigquery for bigquery files "
      ],
      "metadata": {
        "id": "Se7I_DtzES7B"
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib"
      ],
      "metadata": {
        "id": "maQt1jgnExtv"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import xlrd ## import xlrd for excel files, tab names"
      ],
      "metadata": {
        "id": "m4UDofphE3SE"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data = requests.get(https://data.cms.gov/provider-summary-by-type-of-service/medicare-post-acute-care-hospice/medicare-post-acute-care-hospice-by-provider-and-service/data)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 148
        },
        "id": "XJa1-ph6Gw7d",
        "outputId": "09396b80-aaff-4176-d4f6-1ea0778c5e28"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-15-a0de2d5d5028>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    data = requests.get(https://data.cms.gov/provider-summary-by-type-of-service/medicare-post-acute-care-hospice/medicare-post-acute-care-hospice-by-provider-and-service/data)\u001b[0m\n\u001b[0m                             ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "## Error in using data requests"
      ],
      "metadata": {
        "id": "d_UWj8OrG2o9"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}