from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.appName("DockerSpark").getOrCreate()
    
    # Ejemplo básico
    data = [("Python", 1), ("Spark", 2), ("Docker", 3)]
    df = spark.createDataFrame(data, ["Tecnología", "Ranking"])
    df.show()

    # Guardar resultados (opcional)
    df.write.csv("/data/output", mode="overwrite")

if __name__ == "__main__":
    main()
