from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Select relevant features and target
features = ['h1n1_worry', 'h1n1_awareness', 'antiviral_medication', 'contact_avoidance',
            'bought_face_mask', 'wash_hands_frequently', 'avoid_large_gatherings',
            'reduced_outside_home_cont', 'avoid_touch_face', 'dr_recc_h1n1_vacc',
            'dr_recc_seasonal_vacc', 'chronic_medic_condition', 'cont_child_undr_6_mnth',
            'is_health_worker', 'has_health_insur', 'is_h1n1_vacc_effective',
            'is_h1n1_risky', 'sick_from_h1n1_vacc']

X = df[features]
y = df['h1n1_vaccine']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
