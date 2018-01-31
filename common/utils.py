# LEAD MODEL ALL CHOICES LIST

CLIENT_VALUE_CHOICES = (
    ("High", "High"),
    ("Mid", "Mid"),
    ("Low", "Low")
)

SERVICE_TYPE_CHOICES = (
    ("Top Jobs", "Top Jobs"),
    ("Hot Jobs", "Hot Jobs"),
    ("F. Post", "F. Post"),
    ("G. Post", "G. Post")
)

STAGES_CHOICES = (
    ("Lead Generation", "Lead Generation"),
    ("Invoice Approval", "Invoice Approval"),
    ("Job Post", "Job Post"),
    ("Pre Design", "Pre Design"),
    ("Approval On Progress", "Approval On Progress"),
    ("Billing Process", "Billing Process"),
    ("Payment On Progress", "Payment On Progress"),
    ("Payment Received", "Payment Received"),
    ("Payment Verified", "Payment Verified")
)

LAST_STATUS_CHOICES = (
    ("Successful", "Successful"),
    ("Unsuccessful", "Unsuccessful")
)

DISCOUNT_ENTRY_CHOICES = (
    ("Flat", "Flat"),
    ("Percentage", "Percentage")
)

# CLIENT ADDITION CHOICES

EMPLOYEE_SIZE_CHOICES = (
    ("1-10", "1-10"),
    ("10-50", "10-50"),
    ("50-100", "50-100"),
    ("100-500", "100-500"),
    ("500+", "500+")
)

# COMMUNICATION CHOICES

MEDIUM_CHOICES = (
    ("Call", "Call"),
    ("Email", "Email"),
    ("SMS", "SMS"),
    ("Meeting", "Meeting"),
)

MEDIUM_DIRECTION_CHOICES = (
    ("Inbound", "Inbound"),
    ("Outbound", "Outbound")
)

SALES_STAGE_CHOICES = (
    ("Suspecting", "Suspecting"),
    ("Prospecting", "Prospecting"),
    ("Approaching", "Approaching"),
    ("Negotiation", "Negotiation"),
    ("Sales Lead", "Sales Lead"),
    ("Value Proposition", "Value Proposition")
)

# COMMUNICATION SALES STAGES CHOICES

SUSPECTING_CHOICES = (
    ("s1", "Contact Verification"),
)

PROSPECTING_CHOICES = (
    ("p1", "Add Client Detail"),
    ("p2", "Introduce Service"),
    ("p3", "Showed Interest For Now"),
    ("p4", "Showed Interest For Later"),
    ("p5", "Preferred Competitors"),
    ("p6", "Not Interested"),
    ("p7", "Dont Call Me Again"),
    ("p8", "Interest In Other HR Service")
)

APPROACHING_CHOICES = (
    ("a1", "Service Introduction"),
    ("a2", "Business Renewal"),
    ("a3", "Submit Proposal"),
    ("a4", "Presentation")
)

NEGOTIATION_CHOICES = (
    ("n1", "Service Discussion"),
    ("n2", "Discount Discussion")
)
