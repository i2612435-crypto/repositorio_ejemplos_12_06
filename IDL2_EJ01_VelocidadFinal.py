{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNKqB+MSji7iRvDrNl19OKZ",
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
        "<a href=\"https://colab.research.google.com/github/i2612435-crypto/repositorio_ejemplos_12_06/blob/main/IDL2_EJ01_VelocidadFinal.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "D7YnThiqycyK",
        "outputId": "2f312523-b543-487c-9097-8a357b61939c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "=== EJERCICIO 1: VELOCIDAD FINAL ===\n",
            "Velocidad inicial: 0 m/s\n",
            "Aceleración: 0.8 m/s²\n",
            "Tiempo: 30 segundos\n",
            "Velocidad final: 24.0 m/s\n"
          ]
        }
      ],
      "source": [
        "# IDL2 - Ejercicio 1: Velocidad final del auto\n",
        "# Estructura secuencial\n",
        "# Enunciado: Calcular velocidad final con vi=0, a=0.8 m/s², t=30 seg\n",
        "\n",
        "print(\"=== EJERCICIO 1: VELOCIDAD FINAL ===\")\n",
        "vi = 0      # velocidad inicial (m/s)\n",
        "a = 0.8     # aceleración (m/s²)\n",
        "t = 30      # tiempo (segundos)\n",
        "\n",
        "vf = vi + a * t\n",
        "\n",
        "print(f\"Velocidad inicial: {vi} m/s\")\n",
        "print(f\"Aceleración: {a} m/s²\")\n",
        "print(f\"Tiempo: {t} segundos\")\n",
        "print(f\"Velocidad final: {vf} m/s\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "s-y7Shs-0WdD"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}