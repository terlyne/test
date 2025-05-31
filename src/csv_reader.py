def read_csv(filepath: str) -> list[dict[str, str]]:
    """Функция для чтения значений из csv-файла."""
    with open(filepath, "r") as f:
        header = f.readline().strip().split(",")
        data = []
        for line in f:
            values = line.strip().split(",")
            values_dict = {}
            for i in range(len(values)):
                values_dict[header[i]] = values[i]
            data.append(values_dict)
        
        return data
        
