
def generate_bulk_insert_statements(batch_size=10000):
    max_value = 1000  # x, y の最大値
    batches = []

    current_batch = []
    for x in range(max_value):
        for y in range(max_value):
            current_batch.append(f"({x}, {y})")
            if len(current_batch) >= batch_size:
                batches.append(",\n".join(current_batch))
                current_batch = []

    # 残りの部分を追加
    if current_batch:
        batches.append(",\n".join(current_batch))

    return batches

# 生成されたバッチのリストを表示または保存
batches = generate_bulk_insert_statements()
for batch in batches:
    print(f"INSERT INTO field (x, y) VALUES \n{batch};\n")
