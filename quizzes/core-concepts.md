---
title: Core Concepts Quiz
---

## 10 Quick Checks
1. **CIA triad:** Which “C” guards against disclosure?
2. **Vuln vs Threat:** Define each briefly.
3. **Risk calc:** What’s the formula for risk at a high level?
4. **Control types:** Give 1 preventive, 1 detective, 1 corrective.
5. **NIST functions:** List the 5.
6. **AuthN vs AuthZ:** Difference?
7. **Hashing:** Two properties we want?
8. **Symmetric vs Asymmetric:** One use case each.
9. **Ports:** What runs on 22, 53, 80/443?
10. **Logs:** Which log would you check first for failed SSH logins?

*Answer key (fold it under a details block):*
<details>
<summary>Show answers</summary>

1. **Confidentiality**  
2. Vulnerability = weakness; Threat = potential adverse event exploiting a vuln  
3. Risk ≈ Likelihood × Impact  
4. Preventive: firewall rule; Detective: IDS alert; Corrective: restore from backup  
5. Identify, Protect, Detect, Respond, Recover  
6. AuthN = who you are; AuthZ = what you can do  
7. Preimage/collision resistance  
8. Symmetric: bulk data; Asymmetric: key exchange/signing  
9. 22 SSH, 53 DNS, 80/443 HTTP/HTTPS  
10. `/var/log/auth.log` (Debian/Ubuntu) or `/var/log/secure` (RHEL)
</details>
