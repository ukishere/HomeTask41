import datetime

def logger(log_path):
    def decorator_maker(function_for_log):
        def log_writer(*args, **kwargs):
            with open(log_path, 'w') as file:

                file.write(f'Вызов функции: {function_for_log.__name__}\n')
                file.write(f'Начало работы: {datetime.datetime.now()}\n')
                file.write(f'Аргументы функции: {args} {kwargs}\n')

                result = function_for_log(*args, **kwargs)
                file.write(f'Результат работы функции: {result}\n')
                file.write('____________________________\n')
        return log_writer
    return decorator_maker

