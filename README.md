# Vulnerable-API-Security-Lab

##  Objective
This project demonstrates common API security vulnerabilities including:
- Broken Authentication
- Broken Object Level Authorization (BOLA)

---

## 🔓 Vulnerabilities

### 1. Broken Authentication
- Predictable token generation
- No validation or expiration

### 2. BOLA
- Users can access any account by changing ID

---

##  Impact
- Unauthorized access
- Data leakage
- Account compromise

---

##  Mitigation
- Implement strong authentication (JWT)
- Enforce proper authorization checks
- Validate user identity before returning data

---

##  How to Run
1. Install Flask
2. Run 'python app.py'
3. Test endpoints using Postman or browser

---

##  Learning Outcome
This project helped me understand real-world API security vulnerabilities and how attackers exploit insecure endpoints.
