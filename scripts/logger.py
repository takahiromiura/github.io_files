import logging
# ログの出力名を設定
logger = logging.getLogger('LoggingTest')

# ログレベルの設定
logger.setLevel(10)

# ログのファイル出力先を設定
fh = logging.FileHandler('test.log')
logger.addHandler(fh)

# ログのコンソール出力の設定
sh = logging.StreamHandler()
logger.addHandler(sh)

logger.log(20, 'info')
logger.log(30, 'warning')
logger.log(100, 'test')

logger.info('info')
logger.warning('warning')
if __name__=='__main__':

    print('Hello Logger!')
    # print(logger)
