# 個人Blog網站開發

---

## 專案簡介

一個使用 **Flask + MySQL** 開發的個人部落格系統，支援登入、文章發佈、編輯與刪除，介面簡潔直覺，並搭配 Bootstrap 5 進行前端設計。

## 專案功能

- 使用者登入驗證（bcrypt + flask-login）
- 文章 CRUD 功能（Create / Read / Update / Delete）
- Markdown 預覽支援（showdown.js）
- Bootstrap 5 響應式介面
- SQLAlchemy ORM 操作 MySQL 資料庫
- Docker & Docker Compose 一鍵部署

## 快速開始
以下說明將引導你在本地機器上搭建和運行此專案，以便進行開發和測試。

### 環境需求
你的系統上需要安裝 Docker 和 Docker Compose。

- Docker Desktop：https://www.docker.com/products/docker-desktop/

### 安裝步驟
### 1. 複製專案：
```bash
git clone <你的儲存庫網址>
cd <你的儲存庫名稱>
```

### 2.使用 Docker Compose 建立並運行：
```bash
docker-compose up --build
```

### 3.瀏覽網站：
一旦容器啟動並運行，你就可以在瀏覽器中透過以下網址訪問部落格：
http://localhost

---

## 使用說明
### 管理員登入
請注意：此為開發環境的預設帳密。在生產環境中務必修改！

預設的管理員帳密是：root/1234566，您可以透過 http://localhost/login.html 進行登入。
<img width="950" height="337" alt="image" src="https://github.com/user-attachments/assets/020275ae-9dc6-4d81-bdc3-14bdc900cc46" />

---

### 建立/編輯文章

- 登入管理員帳號後，將看到「發布新文章」和編輯、刪除現有文章的選項。
- 文章編輯頁面支援 Markdown 內容撰寫，並包含即時預覽功能。
<img width="935" height="500" alt="image" src="https://github.com/user-attachments/assets/d7c544b8-69ad-4f41-b058-c558c753d2b0" />
<img width="944" height="502" alt="image" src="https://github.com/user-attachments/assets/5ce26507-4b71-44d0-a22d-af62e8ae53c7" />
<img width="944" height="497" alt="image" src="https://github.com/user-attachments/assets/404b5e8d-49f8-4ac7-a328-31b183ca3e05" />

