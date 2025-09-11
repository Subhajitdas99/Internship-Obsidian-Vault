# Weekly Plan – Patient & Doctor Experience

## Table of Contents
1. [Patient Experience](#patient-experience)  
2. [Doctor Experience](#doctor-experience)  

---

## Patient Experience

### Week 1: Registration & Onboarding
**Objectives:** Help patients locate the app, register, verify, and complete onboarding.

**Experience Flow:**  
- Locate the app.  
- Register via email/phone/social login.  
- Verify identity via OTP/email.  
- Complete onboarding walkthrough.

**Technical Implementation:**  
- **Entities:** Patient, Profile, VerificationToken, OnboardingStatus  
- **Relationships:**  
  - Patient ↔ Profile (1:1)  
  - Patient ↔ VerificationToken (1:N)  
  - Patient ↔ OnboardingStatus (1:1)  

**Tasks:**  
- Backend APIs: registration, verification, onboarding status  
- Database tables: patients, profiles, verification_tokens  

---

### Week 2: Appointment Making
**Objectives:** Allow patients to book appointments easily.

**Experience Flow:**  
- Locate doctor by specialty/ratings/availability  
- Select available slot and preferred time  
- Confirm appointment  
- View appointment summary and reminders

**Technical Implementation:**  
- **Entities:** Appointment, Doctor, Patient, Slot, Time  
- **Relationships:**  
  - Appointment ↔ Patient (N:1)  
  - Appointment ↔ Doctor (N:1)  
  - Doctor ↔ Slot (1:N)  
  - Slot ↔ Time (1:N)  

**Tasks:**  
- Backend: APIs for doctor listing, slot selection, time booking, confirmation  

---

### Week 3: Elastic Scheduling
**Objectives:** Implement elastic scheduling for patients to book and adjust appointments dynamically.

**Experience Flow:**  
- Access upcoming appointments  
- View flexible slots available based on doctor availability  
- Confirm or adjust appointment dynamically  

**Technical Implementation:**  
- **Entities:** Appointment, Doctor, Patient, ElasticSlot, SlotAllocation  
- **Relationships:**  
  - Appointment ↔ ElasticSlot (N:1)  
  - Doctor ↔ ElasticSlot (1:N)  
- **Tasks:**  
  - Backend: APIs to fetch elastic slots, create/update appointments  
  - Database: tables for ElasticSlot, SlotAllocation, dynamic slot availability  

---

### Week 4: Elastic Scheduling Enhancements
**Objectives:** Extend elastic scheduling with notifications and analytics.

**Experience Flow:**  
- Track dynamic changes in appointments  
- Notify patients of updated availability  
- Monitor slot utilization and analytics  

**Technical Implementation:**  
- **Entities:** Appointment, Notification, ElasticSlot, Analytics  
- **Relationships:**  
  - Patient ↔ Notification (1:N)  
  - Appointment ↔ Analytics (1:1)  
- **Tasks:**  
  - Backend: scheduled jobs for notifications, elastic slot updates  
  - Database: logging changes, analytics for slot usage  

---

## Doctor Experience

### Week 1: Onboarding & Profile Setup
**Objectives:** Help doctors register, verify credentials, and setup profile.

**Experience Flow:**  
- Locate app  
- Register with professional credentials  
- Verify credentials/approval  
- Setup profile: specialization, experience, consultation hours

**Technical Implementation:**  
- **Entities:** Doctor, Profile, VerificationToken, Specialization  
- **Relationships:**  
  - Doctor ↔ Profile (1:1)  
  - Doctor ↔ VerificationToken (1:N)  
  - Doctor ↔ Specialization (1:N)  

**Tasks:**  
- Backend APIs: registration, verification, profile update  
- Database: doctors, profiles, verification_tokens, specializations  

---

### Week 2: Appointment Management
**Objectives:** Allow doctors to view, confirm, and manage appointments.

**Experience Flow:**  
- View scheduled appointments   
- Update appointment status (Completed/Cancelled)  

**Technical Implementation:**  
- **Entities:** Appointment, Doctor, Patient, Slot, Time  
- **Relationships:**  
  - Doctor ↔ Appointment (1:N)  
  - Appointment ↔ Patient (N:1)  
  - Doctor ↔ Slot (1:N)  
  - Slot ↔ Time (1:N)  

**Tasks:**  
- Backend: APIs for fetching appointments, updating status  

---

### Week 3: Elastic Scheduling
**Objectives:** Implement elastic scheduling for doctors to manage dynamic appointments.

**Experience Flow:**  
- View flexible slots based on doctor availability  
- Confirm, adjust, or free slots dynamically  

**Technical Implementation:**  
- **Entities:** Doctor, Appointment, ElasticSlot, SlotAllocation  
- **Relationships:**  
  - Doctor ↔ ElasticSlot (1:N)  
  - Appointment ↔ ElasticSlot (N:1)  

**Tasks:**  
- Backend: APIs for elastic slot management, update appointment allocations  
- Database: ElasticSlot, SlotAllocation tables  

---

### Week 4: Elastic Scheduling Enhancements
**Objectives:** Enhance elastic scheduling with notifications and analytics for doctors.

**Experience Flow:**  
- Monitor dynamic slot changes  
- Receive notifications on appointment updates  
- Analyze slot utilization and patient engagement  

**Technical Implementation:**  
- **Entities:** Doctor, Appointment, Notification, Analytics, ElasticSlot  
- **Relationships:**  
  - Doctor ↔ Notification (1:N)  
  - Appointment ↔ Analytics (1:1)  

**Tasks:**  
- Backend: APIs for notifications, analytics, dynamic slot updates  
- Database: logging changes and tracking utilization  
