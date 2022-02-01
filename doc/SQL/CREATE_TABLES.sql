CREATE TABLE "User" (                             -- Создаем таблицу.
	"ID"				INTEGER NOT NULL UNIQUE,  -- Создаем числовое поле, обязательно для заполнения, уникальное значение.
	"UserName"			VARCHAR(254) NOT NULL,    -- Создаем текстовое поле, обязательно для заполнения.
	PRIMARY KEY("ID" AUTOINCREMENT)               -- Указываем где ключи 🔑 и поля с счетчиком.
);
CREATE TABLE "Alerts" (                           -- Создаем таблицу.
	"ID"				INTEGER NOT NULL UNIQUE,  -- Создаем числовое поле, обязательно для заполнения, уникальное значение.
	"AlertsType"		VARCHAR(254) NOT NULL,    -- Создаем текстовое поле, обязательно для заполнения.
	"StandardSound"		VARCHAR(254) NOT NULL,    -- Создаем текстовое поле, обязательно для заполнения.
	"OwnSound"			VARCHAR(254),             -- Создаем текстовое поле.
	FOREIGN KEY("ID")	REFERENCES "User"("ID"),  -- Указываем какое поле имеет связь с полем из другой талблицы.
	PRIMARY KEY("ID" AUTOINCREMENT)               -- Указываем где ключи 🔑 и поля с счетчиком.
);
CREATE TABLE "Autorun" (                          -- Создаем таблицу.
	"ID"				INTEGER NOT NULL UNIQUE,  -- Создаем числовое поле, обязательно для заполнения, уникальное значение.
	"EnableProgram"		INTEGER NOT NULL,         -- Создаем числовое поле, обязательно для заполнения.
	"EnableMic"			INTEGER NOT NULL,         -- Создаем числовое поле, обязательно для заполнения.
	FOREIGN KEY("ID")	REFERENCES "User"("ID"),  -- Указываем какое поле имеет связь с полем из другой талблицы.
	PRIMARY KEY("ID" AUTOINCREMENT)               -- Указываем где ключи 🔑 и поля с счетчиком.
);
CREATE TABLE "Hotkey" (                           -- Создаем таблицу.
	"ID"				INTEGER NOT NULL UNIQUE,  -- Создаем числовое поле, обязательно для заполнения, уникальное значение.
	"HotkeyMic"			VARCHAR(32),              -- Создаем текстовое поле.
	"HotkeyWalkie"		VARCHAR(32),              -- Создаем текстовое поле.
	FOREIGN KEY("ID")	REFERENCES "User"("ID"),  -- Указываем какое поле имеет связь с полем из другой талблицы.
	PRIMARY KEY("ID" AUTOINCREMENT)               -- Указываем где ключи 🔑 и поля с счетчиком.
);
CREATE TABLE "Settings" (                         -- Создаем таблицу.
	"ID"				INTEGER NOT NULL UNIQUE,  -- Создаем числовое поле, обязательно для заполнения, уникальное значение.
	"LanguageCode"		VARCHAR(4) NOT NULL,      -- Создаем текстовое поле, обязательно для заполнения.
	"NightTheme"		INTEGER NOT NULL,         -- Создаем числовое поле, обязательно для заполнения.
	FOREIGN KEY("ID")	REFERENCES "User"("ID"),  -- Указываем какое поле имеет связь с полем из другой талблицы.
	PRIMARY KEY("ID" AUTOINCREMENT)               -- Указываем где ключи 🔑 и поля с счетчиком.
);
CREATE TABLE "About" (                            -- Создаем таблицу.
	"ID"				INTEGER NOT NULL UNIQUE,  -- Создаем числовое поле, обязательно для заполнения, уникальное значение.
	"ProgramVersion"	VARCHAR(32) NOT NULL,     -- Создаем текстовое поле, обязательно для заполнения.
	"WebSite"			VARCHAR(32) NOT NULL,     -- Создаем текстовое поле, обязательно для заполнения.
	"Email"				VARCHAR(32) NOT NULL,     -- Создаем текстовое поле, обязательно для заполнения.
	"Copyright"			VARCHAR(64) NOT NULL,     -- Создаем текстовое поле, обязательно для заполнения.
	"UrlPrivacyPolicy"	VARCHAR(64) NOT NULL,     -- Создаем текстовое поле, обязательно для заполнения.
	PRIMARY KEY("ID" AUTOINCREMENT)               -- Указываем где ключи 🔑 и поля с счетчиком.
);

