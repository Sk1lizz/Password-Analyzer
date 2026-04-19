ru_RU = '''# Языковой файл для Password Analyzer
# Версия: 1.0.0
# Язык: Русский

meta:
  language: "Русский"
  code: "ru-RU"
  author: "skilizz"
  version: "1.0.0"
  last_update: "19.04.2026"


# ==========================================================
# =================== Основные надписи =====================
# ==========================================================


app:
  name: "PasswordAnalyzer"
  title: "🔐 Анализатор паролей 🔐"
  waiting-message: "Введите пароль..."
  result-text: "Результат: "

  full-text: "📊 Детальный анализ:"
  text-result-full: 
    len: "Длина: <len> <suffix>"
    len-suffix:
      0: "символ"
      1: "символа"
      2: "символов"
    upper: "Заглавные буквы: A-Z"
    lower: "Строчные буквы: a-z"
    number: "Цифры: 0-9"
    special: "Спецсимволы: !@#$%"
    entropy: "Энтропия: <entropy> бит"

    liked-password: "Схожесть с популярными паролями: "
    result-liked: "Статус: <status>"
    result-liked-password:
      0: "Отсутствует"
      1: "Похож"
      2: "Точное совпадение"
    if-liked: "Пароль похож на"

    power-password: "💪 Надёжность: "
  
  status-text: 
    -1: "Ошибка"        
    0: "Ужасный пароль"               
    1: "Очень плохой пароль"
    2: "Плохой пароль"
    3: "Нормальный пароль"
    4: "Хороший пароль"
    5: "Отличный пароль"
    6: "Превосходный пароль"
    7: "Самый защищённый пароль"
  
  status:
    -1: "ОШИБКА"
    0: "УЖАСНО"
    1: "УЖАСНО"
    2: "ПЛОХО"
    3: "НОРМАЛЬНО"
    4: "ХОРОШИЙ"
    5: "ОТЛИЧНО"
    6: "ОТЛИЧНО"
    7: "ПРЕВОСХОДНО"

  button-text:
    setting: "⚙️ Настройки"
    generate: "🎲 Генерация"
    history: "📜 История"
    show-password: "🔓 Показать пароль"
    hide-password: "🔒 Скрыть пароль"
    copy: "📋 Скопировать"
    successful-copy: "✅ Скопировано!"

setting:
  name: "PasswordAnalyzer - settings"
  title: "Настройки"
  title-theme: "Тема оформления:"
  theme:
    light: "Светлая"
    dark: "Тёмная"
    system: "Как в системе"
  title-history: "Максимум записей в истории:"
  title-language: "Язык:"
  waiting-message: "Выберите язык"
  button-save: "Сохранить изменения"
  successful-save: "✅ Настройки применены!"
  

generate:
  name: "PasswordAnalyzer - generate"
  title: "🔐 Генератор паролей 🔐"
  button:
    generate: "🎲 Генерация"
    setting: "⚙️ Настройки"
    main-app: "🔐 Анализатор"
    history: "📜 История"
    copy: "📋 Скопировать"
    successful-copy: "✅ Скопировано!"

  text-result-full:
    len: "<len> симв."
    upper: "Использовать заглавные буквы"
    lower: "Использовать строчные буквы"
    custom: "Использовать русские буквы"
    number: "Использовать числа"
    special: "Использовать спецсимволы"
    error: "❌ Невозможно сгенерировать пароль"
    

history: 
  name: "PasswordAnalyzer - history"
  title: "📜 История проверок 📜"

  table:
    date: "🕐 Дата/Время"
    password: "🔒 Пароль"
    result-password: "💪 Оценка"
    entropy: "📊 Энтропия"

  name-result:
    strong: "🎯 Сильный"
    medium: "🔸 Средний"
    weak: "⚠️ Слабый"
    bad: "💩 Ужасный"

  bit: "<len> бит"


  result: "📊 Всего: <len_total>  │ 🎯 <len_strong>  │ 🔸 <len_medium>  │ ⚠️ <len_weak> │ 💩 <len_bad>"

  button:
    clear: "🗑️ Очистить историю"
    copy: "📋 Копировать"
    successful-copy: "✅ Скопировано!"

  message-box:
    title: "Подтверждение"
    text: "Вы уверены?"
    button: 
      yes_btn: "✅ Да, уверен"
      no_btn: "❌ Нет, отмена"'''


en_EN = '''# Language file for Password Analyzer
# Version: 1.0.0
# Language: English

meta:
  language: "English"
  code: "en-EN"
  author: "skilizz"
  version: "1.0.0"
  last_update: "19.04.2026"


# ==========================================================
# =================== Main Labels ==========================
# ==========================================================


app:
  name: "PasswordAnalyzer"
  title: "🔐 Password Analyzer 🔐"
  waiting-message: "Enter password..."
  result-text: "Result: "

  full-text: "📊 Detailed analysis:"
  text-result-full: 
    len: "Length: <len> <suffix>"
    len-suffix:
      0: "character"
      1: "characters"
      2: "characters"
    upper: "Uppercase letters: A-Z"
    lower: "Lowercase letters: a-z"
    number: "Digits: 0-9"
    special: "Special characters: !@#$%"
    entropy: "Entropy: <entropy> bits"

    liked-password: "Similarity to common passwords: "
    result-liked: "Status: <status>"
    result-liked-password:
      0: "None"
      1: "Similar"
      2: "Exact match"
    if-liked: "Password is similar to"

    power-password: "💪 Strength: "
  
  status-text: 
    -1: "Error"        
    0: "Terrible password"               
    1: "Very bad password"
    2: "Bad password"
    3: "Normal password"
    4: "Good password"
    5: "Excellent password"
    6: "Superb password"
    7: "Most secure password"
  
  status:
    -1: "ERROR"
    0: "TERRIBLE"
    1: "TERRIBLE"
    2: "BAD"
    3: "NORMAL"
    4: "GOOD"
    5: "EXCELLENT"
    6: "EXCELLENT"
    7: "SUPERB"

  button-text:
    setting: "⚙️ Settings"
    generate: "🎲 Generate"
    history: "📜 History"
    show-password: "🔓 Show password"
    hide-password: "🔒 Hide password"
    copy: "📋 Copy"
    successful-copy: "✅ Copied!"

setting:
  name: "PasswordAnalyzer - settings"
  title: "Settings"
  title-theme: "Theme:"
  theme:
    light: "Light"
    dark: "Dark"
    system: "System default"
  title-history: "Max history entries:"
  title-language: "Language:"
  waiting-message: "Select language"
  button-save: "Save changes"
  successful-save: "✅ Settings applied!"
  

generate:
  name: "PasswordAnalyzer - generate"
  title: "🔐 Password Generator 🔐"
  button:
    generate: "🎲 Generate"
    setting: "⚙️ Settings"
    main-app: "🔐 Analyzer"
    history: "📜 History"
    copy: "📋 Copy"
    successful-copy: "✅ Copied!"

  text-result-full:
    len: "<len> chars"
    upper: "Use uppercase letters"
    lower: "Use lowercase letters"
    custom: "Use Russian letters"
    number: "Use numbers"
    special: "Use special characters"
    error: "❌ Cannot generate password"    

history: 
  name: "PasswordAnalyzer - history"
  title: "📜 Password History 📜"

  table:
    date: "🕐 Date/Time"
    password: "🔒 Password"
    result-password: "💪 Strength"
    entropy: "📊 Entropy"

  name-result:
    strong: "🎯 Strong"
    medium: "🔸 Medium"
    weak: "⚠️ Weak"
    bad: "💩 Terrible"

  bit: "<len> bits"

  result: "📊 Total: <len_total>  │ 🎯 <len_strong>  │ 🔸 <len_medium>  │ ⚠️ <len_weak> │ 💩 <len_bad>"

  button:
    clear: "🗑️ Clear history"
    copy: "📋 Copy"
    successful-copy: "✅ Copied!"

  message-box:
    title: "Confirmation"
    text: "Are you sure?"
    button: 
      yes_btn: "✅ Yes, I'm sure"
      no_btn: "❌ No, cancel"'''

zn_CH = '''# 密码分析器的语言文件
# 版本: 1.0.0
# 语言: 简体中文

meta:
  language: "简体中文"
  code: "zh-CN"
  author: "skilizz"
  version: "1.0.0"
  last_update: "2026.04.15"


# ==========================================================
# =================== 主要标签 =============================
# ==========================================================


app:
  name: "PasswordAnalyzer"
  title: "🔐 密码分析器 🔐"
  waiting-message: "请输入密码..."
  result-text: "结果: "

  full-text: "📊 详细分析:"
  text-result-full: 
    len: "长度: <len> 个字符"
    len-suffix:
      0: "字符"
      1: "字符"
      2: "字符"
    upper: "大写字母: A-Z"
    lower: "小写字母: a-z"
    number: "数字: 0-9"
    special: "特殊字符: !@#$%"
    entropy: "熵: <entropy> 比特"

    liked-password: "与常见密码的相似度: "
    result-liked: "状态: <status>"
    result-liked-password:
      0: "无"
      1: "相似"
      2: "完全匹配"
    if-liked: "密码类似于"

    power-password: "💪 强度: "
  
  status-text: 
    -1: "错误"        
    0: "糟糕的密码"               
    1: "非常差的密码"
    2: "差密码"
    3: "普通密码"
    4: "好密码"
    5: "优秀的密码"
    6: "极好的密码"
    7: "最安全的密码"
  
  status:
    -1: "错误"
    0: "糟糕"
    1: "糟糕"
    2: "差"
    3: "普通"
    4: "好"
    5: "优秀"
    6: "优秀"
    7: "极好"

  button-text:
    setting: "⚙️ 设置"
    generate: "🎲 生成"
    history: "📜 历史记录"
    show-password: "🔓 显示密码"
    hide-password: "🔒 隐藏密码"
    copy: "📋 复制"
    successful-copy: "✅ 已复制！"

setting:
  name: "PasswordAnalyzer - 设置"
  title: "设置"
  title-theme: "主题:"
  theme:
    light: "浅色"
    dark: "深色"
    system: "跟随系统"
  title-history: "最大历史记录数:"
  title-language: "语言:"
  waiting-message: "选择语言"
  button-save: "保存更改"
  successful-save: "✅ 设置已应用！"
  

generate:
  name: "PasswordAnalyzer - 生成器"
  title: "🔐 密码生成器 🔐"
  button:
    generate: "🎲 生成"
    setting: "⚙️ 设置"
    main-app: "🔐 分析器"
    history: "📜 历史记录"
    copy: "📋 复制"
    successful-copy: "✅ 已复制！"

  text-result-full:
    len: "<len> 个字符"
    upper: "使用大写字母"
    lower: "使用小写字母"
    custom: "使用俄文字母"
    number: "使用数字"
    special: "使用特殊字符"
    error: "❌ 无法生成密码"    

history: 
  name: "PasswordAnalyzer - 历史记录"
  title: "📜 密码历史记录 📜"

  table:
    date: "🕐 日期/时间"
    password: "🔒 密码"
    result-password: "💪 强度"
    entropy: "📊 熵"

  name-result:
    strong: "🎯 强"
    medium: "🔸 中等"
    weak: "⚠️ 弱"
    bad: "💩 糟糕"

  bit: "<len> 比特"

  result: "📊 总计: <len_total>  │ 🎯 <len_strong>  │ 🔸 <len_medium>  │ ⚠️ <len_weak> │ 💩 <len_bad>"

  button:
    clear: "🗑️ 清空历史记录"
    successful-clear: ""
    copy: "📋 复制"
    successful-copy: "✅ 已复制！"

  message-box:
    title: "确认"
    text: "您确定吗？"
    button: 
      yes_btn: "✅ 确定"
      no_btn: "❌ 取消"'''