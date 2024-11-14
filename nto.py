def simulate_code_attempts(total_combinations=256, combinations_per_minute=4, wait_time=2):
    remaining_combinations = total_combinations  
    total_minutes_passed = 0  
    attempts_made = 0  

    while remaining_combinations > 0:
        total_minutes_passed += 1
                attempts_this_minute = min(combinations_per_minute, remaining_combinations)
        remaining_combinations -= attempts_this_minute
        attempts_made += attempts_this_minute

        print(f"Минута {total_minutes_passed}: проверка {attempts_this_minute} комбинаций, остаётся {remaining_combinations} комбинаций")

        if attempts_this_minute == combinations_per_minute:
            print(f"Ожидание в течение {wait_time} минут...")
            total_minutes_passed += wait_time
            print("Продолжаем ввод...")

simulate_code_attempts()
