PURCHASE_LOCATION = [
    ('store', 'In-Store'),
    ('online', 'Online'),
    ('vendor', 'Vendor Direct'),
    ('marketplace', 'Marketplace'),
    ('catalog', 'Catalog'),
    ('mobile_app', 'Mobile App'),
    ('social_media', 'Social Media'),
    ('auction', 'Auction'),
    ('subscription', 'Subscription Service'),
    ('popup_shop', 'Pop-Up Shop'),
    ('event', 'Event'),
    ('tv_shopping', 'TV Shopping'),
    ('wholesale', 'Wholesale'),
    ('secondhand', 'Secondhand Marketplace'),
    ('trade_show', 'Trade Show'),
    ('direct_mail', 'Direct Mail'),
    ('telephone_order', 'Telephone Order'),
    ('airport_duty_free', 'Airport Duty-Free'),
    ('inflight', 'In-Flight'),
    ('charity_event', 'Charity Event'),
    ('group_buying', 'Group Buying'),
    ('gift_registry', 'Gift Registry'),
    ('loyalty_program', 'Loyalty Program'),
    ('personal_shopper', 'Personal Shopper'),
    ('rental', 'Rental Service'),
    ('custom_order', 'Custom Order'),
    ('pickup_point', 'Pick-Up Point'),
    ('concierge', 'Concierge Service'),
    ('self_service_kiosk', 'Self-Service Kiosk'),
    ('virtual_store', 'Virtual Store'),
    ('blockchain_marketplace', 'Blockchain Marketplace'),
    ('interactive_television', 'Interactive Television'),
    ('instant_messaging', 'Instant Messaging'),
    ('chatbot', 'Chatbot'),
    ('third_party_website', 'Third-Party Website'),
    ('loyalty_points', 'Loyalty Points Redemption'),
    ('outlet_store', 'Outlet Store'),
]

PAYMENT_METHODS = [
    ('card', 'Credit/Debit Card'),
    ('cash', 'Cash'),
    ('paypal', 'PayPal'),
    ('bank_transfer', 'Bank Transfer'),
    ('apple_pay', 'Apple Pay'),
    ('google_pay', 'Google Pay'),
    ('amazon_pay', 'Amazon Pay'),
    ('crypto', 'Cryptocurrency'),
    ('installments', 'Installments'),
    ('check', 'Check'),
    ('money_order', 'Money Order'),
]

ISSUE_STATUS = [
    ('0000', 'Processing'),
    ('0001', 'Failed'),
    ('0002', 'Passed'),
    ('0003', 'Under Review'),
    ('0004', 'Resolved'),
    ('0005', 'Closed'),
    ('0006', 'On Hold'),
    ('0007', 'Canceled'),
    ('0008', 'Pending'),
    ('0009', 'Awaiting Action'),
    ('0010', 'Completed'),
    ('0011', 'Pending Review'),
    ('0012', 'Waiting'),
    ('0013', 'Investigating'),
    ('0014', 'Approved'),
    ('0015', 'Rejected'),
    ('0016', 'Escalated'),
    ('0017', 'In Progress'),
    ('0018', 'Deferred'),
    ('0019', 'Suspended'),
    ('0020', 'Ready'),
]


ISSUE_TYPES = [
    ('DEFECTIVE', 'Defective Unit'),
    ('WRONG UNIT', 'Wrong Unit'),
    ('MISSING PARTS', 'Missing Parts'),
    ('DAMAGED', 'Damaged'),
    ('LATE DELIVERY', 'Late Delivery'),
    ('POOR QUALITY', 'Poor Quality'),
    ('INCORRECT ITEM', 'Incorrect Item'),
    ('SIZE ISSUE', 'Size Issue'),
    ('COLOR ISSUE', 'Color Issue'),
    ('FITTING ISSUE', 'Fitting Issue'),
    ('PACKAGING ISSUE', 'Packaging Issue'),
    ('RETURN REQUEST', 'Return Request'),
    ('EXCHANGE REQUEST', 'Exchange Request'),
    ('REFUND REQUEST', 'Refund Request'),
    ('CANCELATION REQUEST', 'Cancellation Request'),
    ('BILLING ERROR', 'Billing Error'),
    ('CUSTOMER SERVICE ISSUE', 'Customer Service Issue'),
    ('SHIPPING ERROR', 'Shipping Error'),
    ('PAYMENT ISSUE', 'Payment Issue'),
    ('LOYALTY PROGRAM ISSUE', 'Loyalty Program Issue'),
    ('WEBSITE ERROR', 'Website Error'),
    ('APP ERROR', 'App Error'),
    ('SECURITY CONCERN', 'Security Concern'),
    ('PRIVACY CONCERN', 'Privacy Concern'),
    ('COMMUNICATION ISSUE', 'Communication Issue'),
    ('TERMS OF SERVICE VIOLATION', 'Terms of Service Violation'),
    ('OTHER', 'Other Reason'),
]

DELIVERY_STATUS = [
    ('Preparing for Shipment', '0001'),
    ('Shipped', '0002'),
    ('Out for Delivery', '0003'),
    ('Delivered', '0004'),
    ('Delayed', '0005'),
    ('Arrived at Warehouse', '0006'),
    ('Sorting in Progress', '0007'),
    ('In Transit', '0008'),
    ('Awaiting Pickup', '0009'),
    ('On Hold', '0010'),
    ('Attempted Delivery', '0011'),
    ('Returned to Sender', '0012'),
    ('Lost in Transit', '0013'),
    ('Damaged in Transit', '0014'),
    ('Customs Clearance', '0015'),
    ('Scheduled for Delivery', '0016'),
    ('Rescheduled Delivery', '0017'),
    ('Refused Delivery', '0018'),
    ('Address Verification', '0019'),
    ('Package Stolen', '0020'),
    ('Undeliverable', '0021'),
    ('Signature Required', '0022'),
    ('Completed', '0023'),
    ('In Progress', '0024'),
    ('Canceled', '0025'),
]

DAMAGE_SOURCE = [
    ('1001', 'Customer Damage'),
    ('1002', 'Vendor Damage'),
    ('1003', 'Retail Damage'),
    ('1004', 'Shipping Damage'),
    ('1005', 'Manufacturing Defect'),
    ('1006', 'Handling Error'),
    ('1007', 'Natural Disaster'),
    ('1008', 'Wear and Tear'),
    ('1009', 'Storage Damage'),
    ('1010', 'Accidental Damage'),
    ('1011', 'Vandalism'),
    ('1012', 'Theft'),
    ('1013', 'Fire Damage'),
    ('1014', 'Water Damage'),
    ('1015', 'Electrical Damage'),
    ('1016', 'Structural Damage'),
    ('1017', 'Environmental Damage'),
    ('1018', 'Other'),
]
product_categories = [
    ('HOME DECOR', 'Home Decor'),
    ('APPLIANCES', 'Appliances'),
    ('ELECTRONICS', 'Electronics'),
    ('ACCESSORIES', 'Accessories'),
    ('FURNITURE', 'Furniture'),
    ('LIGHTING', 'Lighting'),
    ('TEXTILES', 'Textiles'),
    ('KITCHENWARE', 'Kitchenware'),
    ('TABLEWARE', 'Tableware'),
    ('DECORATIVE ACCENTS', 'Decorative Accents'),
    ('GARDEN & OUTDOOR', 'Garden & Outdoor'),
    ('BEDDING', 'Bedding'),
    ('BATH', 'Bath'),
    ('STORAGE & ORGANIZATION', 'Storage & Organization'),
    ('PET SUPPLIES', 'Pet Supplies'),
    ('BABY & KIDS', 'Baby & Kids'),
    ('OFFICE & SCHOOL SUPPLIES', 'Office & School Supplies'),
    ('CLOTHING & APPAREL', 'Clothing & Apparel'),
    ('SHOES & ACCESSORIES', 'Shoes & Accessories'),
    ('BEAUTY & PERSONAL CARE', 'Beauty & Personal Care'),
    ('HEALTH & WELLNESS', 'Health & Wellness'),
    ('SPORTS & OUTDOORS', 'Sports & Outdoors'),
    ('TRAVEL & LUGGAGE', 'Travel & Luggage'),
    ('HOBBIES & CRAFTS', 'Hobbies & Crafts'),
    ('BOOKS & MAGAZINES', 'Books & Magazines'),
    ('MUSIC & INSTRUMENTS', 'Music & Instruments'),
    ('ART & COLLECTIBLES', 'Art & Collectibles'),
    ('GIFTS & OCCASIONS', 'Gifts & Occasions'),
    ('PARTY SUPPLIES', 'Party Supplies'),
    ('FOOD & BEVERAGES', 'Food & Beverages'),
    ('RESTAURANT & CATERING', 'Restaurant & Catering'),
    ('HOME IMPROVEMENT', 'Home Improvement'),
    ('AUTOMOTIVE', 'Automotive'),
    ('TOOLS & EQUIPMENT', 'Tools & Equipment'),
    ('ELECTRICAL & LIGHTING', 'Electrical & Lighting'),
    ('PLUMBING & FIXTURES', 'Plumbing & Fixtures'),
    ('BUILDING MATERIALS', 'Building Materials'),
    ('SAFETY & SECURITY', 'Safety & Security'),
    ('FARMING & AGRICULTURE', 'Farming & Agriculture'),
    ('INDUSTRIAL SUPPLIES', 'Industrial Supplies'),
    ('OFFICE FURNITURE & SUPPLIES', 'Office Furniture & Supplies'),
    ('COMMERCIAL EQUIPMENT', 'Commercial Equipment'),
    ('PACKAGING & SHIPPING', 'Packaging & Shipping'),
    ('RETAIL DISPLAYS & FIXTURES', 'Retail Displays & Fixtures'),
    ('SERVICES & CONTRACTING', 'Services & Contracting'),
    ('EVENT PLANNING & SERVICES', 'Event Planning & Services'),
]


product_materials = [
    ('PLASTIC', 'plastic'),
    ('METAL', 'material'),
    ('GLASS', 'glass'),
    ('HYBRID', 'Hybrid'),
    ('WOOD', 'wood'),
    ('CERAMIC', 'ceramic'),
    ('PAPER', 'paper'),
    ('FABRIC', 'fabric'),
    ('LEATHER', 'leather'),
    ('RUBBER', 'rubber'),
    ('STONE', 'stone'),
    ('CONCRETE', 'concrete'),
    ('COMPOSITE', 'composite'),
    ('ALUMINUM', 'aluminum'),
    ('STAINLESS STEEL', 'stainless steel'),
    ('CARBON FIBER', 'carbon fiber'),
    ('BAMBOO', 'bamboo'),
    ('CORK', 'cork'),
    ('SYNTHETIC', 'synthetic'),
    ('VINYL', 'vinyl'),
    ('POLYMER', 'polymer'),
    ('SILICONE', 'silicone'),
    ('NATURAL FIBER', 'natural fiber'),
    ('PLANT-BASED', 'plant-based'),
    ('RECYCLED', 'recycled'),
    ('BIODEGRADABLE', 'biodegradable'),
    ('ELECTRONIC', 'electronic'),
    ('TEXTILE', 'textile'),
    ('SILK', 'silk'),
    ('WOOL', 'wool'),
    ('LINEN', 'linen'),
    ('ALLOY', 'alloy'),
    ('BRASS', 'brass'),
    ('BRONZE', 'bronze'),
    ('COPPER', 'copper'),
    ('GOLD', 'gold'),
    ('SILVER', 'silver'),
    ('TITANIUM', 'titanium'),
    ('ZINC', 'zinc'),
    ('NICKEL', 'nickel'),
    ('PLATINUM', 'platinum'),
    ('MAGNESIUM', 'magnesium'),
    ('TUNGSTEN', 'tungsten'),
    ('IRON', 'iron'),
    ('STEEL', 'steel'),
    ('CAST IRON', 'cast iron'),
    ('WROUGHT IRON', 'wrought iron'),
    ('TIN', 'tin'),
    ('POLYPROPYLENE', 'polypropylene'),
    ('POLYETHYLENE', 'polyethylene'),
    ('POLYSTYRENE', 'polystyrene'),
    ('ACRYLIC', 'acrylic'),
    ('NYLON', 'nylon'),
    ('POLYESTER', 'polyester'),
    ('RAYON', 'rayon'),
    ('SATIN', 'satin'),
    ('VELVET', 'velvet'),
    ('DENIM', 'denim'),
    ('CORDUROY', 'corduroy'),
    ('LACE', 'lace'),
    ('CHIFFON', 'chiffon'),
    ('ORGANZA', 'organza'),
    ('TAFFETA', 'taffeta'),
    ('TWILL', 'twill'),
    ('CHAMBRAY', 'chambray'),
    ('FLANNEL', 'flannel'),
    ('SEERSUCKER', 'seersucker'),
    ('JERSEY', 'jersey'),
    ('FLEECE', 'fleece'),
    ('VELOUR', 'velour'),
    ('MOLESKIN', 'moleskin'),
    ('CORDUROY', 'corduroy'),
    ('SUEDE', 'suede'),
    ('LEATHERETTE', 'leatherette'),
    ('NEOPRENE', 'neoprene'),
    ('MICROFIBER', 'microfiber'),
    ('VELVETEEN', 'velveteen'),
    ('BURLAP', 'burlap'),
    ('TWINE', 'twine'),
    ('JUTE', 'jute'),
    ('LINOLEUM', 'linoleum'),
    ('LAMINATE', 'laminate'),
    ('VENEER', 'veneer'),
    ('MARBLE', 'marble'),
    ('GRANITE', 'granite'),
    ('SLATE', 'slate'),
    ('QUARTZ', 'quartz'),
    ('SANDSTONE', 'sandstone'),
    ('LIMESTONE', 'limestone'),
    ('BASALT', 'basalt'),
    ('PORCELAIN', 'porcelain'),
    ('ENAMEL', 'enamel'),
    ('GLAZED', 'glazed'),
    ('CERAMIC', 'ceramic'),
    ('TERRACOTTA', 'terracotta'),
    ('CLAY', 'clay'),
    ('GEMSTONE', 'gemstone'),
    ('CRYSTAL', 'crystal'),
    ('DIAMOND', 'diamond'),
    ('RUBY', 'ruby'),
    ('EMERALD', 'emerald'),
    ('SAPPHIRE', 'sapphire'),
    ('TOPAZ', 'topaz'),
    ('AMETHYST', 'amethyst'),
    ('OPAL', 'opal'),
    ('PEARL', 'pearl'),
    ('AGATE', 'agate'),
    ('JASPER', 'jasper'),
    ('LAPIS LAZULI', 'lapis lazuli'),
    ('MALACHITE', 'malachite'),
    ('OBSIDIAN', 'obsidian'),
    ('ONYX', 'onyx'),
    ('QUARTZITE', 'quartzite'),
    ('TURQUOISE', 'turquoise'),
    ('FLUORITE', 'fluorite'),
    ('ZIRCON', 'zircon'),
    ('AMBER', 'amber'),
    ('CORAL', 'coral'),
    ('IVORY', 'ivory'),
    ('BONE', 'bone'),
    ('HORN', 'horn'),
    ('FEATHER', 'feather'),
    ('FUR', 'fur'),
    ('HAIR', 'hair'),
    ('SHELL', 'shell'),
    ('CORK', 'cork'),
    ('BAMBOO', 'bamboo'),
    ('PAPERBOARD', 'paperboard'),
    ('CARDBOARD', 'cardboard'),
    ('HARDWOOD', 'hardwood'),
    ('SOFTWOOD', 'softwood'),
    ('PLYWOOD', 'plywood'),
    ('CHIPBOARD', 'chipboard'),
    ('MDF', 'MDF'),
    ('OSB', 'OSB'),
    ('CHIPBOARD', 'chipboard'),
    ('HDF', 'HDF'),
    ('PVC', 'PVC'),
    ('UPVC', 'UPVC'),
    ('CPVC', 'CPVC'),
    ('ABS', 'ABS'),
    ('PC', 'PC'),
    ('PMMA', 'PMMA'),
    ('PU', 'PU'),
    ('EVA', 'EVA'),
    ('PP', 'PP'),
    ('PE', 'PE'),
    ('PS', 'PS'),
    ('PET', 'PET'),
    ('PBT', 'PBT'),
    ('POM', 'POM'),
    ('PA', 'PA'),
    ('PTFE', 'PTFE'),
    ('PVC', 'PVC'),
    ('HDPE', 'HDPE'),
    ('LDPE', 'LDPE'),
    ('LLDPE', 'LLDPE'),
    ('PVDF', 'PVDF'),
    ('PPS', 'PPS'),
    ('PI', 'PI'),
    ('PUR', 'PUR'),
    ('TPU', 'TPU'),
    ('TPV', 'TPV'),
    ('TPO', 'TPO'),
    ('TPE', 'TPE'),
    ('TPEE', 'TPEE'),
    ('TPX', 'TPX'),
    ('PMMA', 'PMMA'),
    ('PVB', 'PVB'),
    ('PHA', 'PHA'),
    ('PBS', 'PBS'),
    ('PLA', 'PLA'),
    ('PHB', 'PHB'),
    ('PHBV', 'PHBV'),
    ('PHBH', 'PHBH'),
    ('PBSA', 'PBSA'),
    ('PBAT', 'PBAT'),
    ('PEF', 'PEF'),
    ('PVOH', 'PVOH'),
    ('PTT', 'PTT'),
    ('PBST', 'PBST'),
    ('PCL', 'PCL'),
    ('TPE-S', 'TPE-S'),
    ('TPE-V', 'TPE-V'),
    ('TPE-A', 'TPE-A'),
    ('TPE-O', 'TPE-O'),
    ('TPE-F', 'TPE-F'),
    ('TPE-U', 'TPE-U'),
    ('TPE-X', 'TPE-X'),
    ('TPE-Y', 'TPE-Y'),
    ('TPE-Z', 'TPE-Z'),
    ('TPS', 'TPS'),
    ('TPX', 'TPX'),
    ('TPL', 'TPL'),
    ('TPM', 'TPM'),
    ('TPS', 'TPS'),
    ('TPI', 'TPI'),
    ('TPP', 'TPP'),
    ('TPH', 'TPH'),
    ('TPT', 'TPT'),
    ('TPC', 'TPC'),
    ('TPU', 'TPU'),
    ('TPP', 'TPP'),]

area_of_use = [
    ('HOUSE_01', 'Living Room'),
    ('HOUSE_02', 'Kitchen'),
    ('HOUSE_03', 'Bedroom'),
    ('HOUSE_04', 'Bathroom'),
    ('OFFICE_01', 'Office'),
    ('OUTDOOR_01', 'Patio'),
    ('OUTDOOR_02', 'Garden'),
    ('OUTDOOR_03', 'Backyard'),
    ('OUTDOOR_04', 'Poolside'),
    ('OUTDOOR_05', 'Balcony'),
    ('COMMERCIAL_01', 'Retail Store'),
    ('COMMERCIAL_02', 'Restaurant'),
    ('COMMERCIAL_03', 'Hotel'),
    ('COMMERCIAL_04', 'Office Building'),
    ('COMMERCIAL_05', 'Hospital'),
    ('COMMERCIAL_06', 'School'),
    ('COMMERCIAL_07', 'Airport'),
    ('COMMERCIAL_08', 'Shopping Mall'),
    ('COMMERCIAL_09', 'Gym/Fitness Center'),
    ('COMMERCIAL_10', 'Theater/Cinema'),
    ('COMMERCIAL_11', 'Convention Center'),
    ('COMMERCIAL_12', 'Warehouse'),
    ('COMMERCIAL_13', 'Factory'),
    ('COMMERCIAL_14', 'Stadium/Arena'),
    ('COMMERCIAL_15', 'Amusement Park'),
    ('COMMERCIAL_16', 'Museum'),
    ('COMMERCIAL_17', 'Library'),
    ('COMMERCIAL_18', 'Bank'),
    ('COMMERCIAL_19', 'Gas Station'),
    ('COMMERCIAL_20', 'Car Dealership'),
    ('HEALTHCARE_01', 'Doctor\'s Office'),
    ('HEALTHCARE_02', 'Dental Office'),
    ('HEALTHCARE_03', 'Pharmacy'),
    ('HEALTHCARE_04', 'Hospital Room'),
    ('HEALTHCARE_05', 'Operating Room'),
    ('HEALTHCARE_06', 'Laboratory'),
    ('HEALTHCARE_07', 'Clinic'),
    ('HEALTHCARE_08', 'Emergency Room'),
    ('HEALTHCARE_09', 'Intensive Care Unit (ICU)'),
    ('HEALTHCARE_10', 'Radiology Department'),
    ('HEALTHCARE_11', 'Physical Therapy Center'),
    ('HEALTHCARE_12', 'Mental Health Facility'),
    ('HEALTHCARE_13', 'Nursing Home'),
    ('HEALTHCARE_14', 'Assisted Living Facility'),
    ('HEALTHCARE_15', 'Hospice Care Center'),
    ('HEALTHCARE_16', 'Rehabilitation Center'),
]