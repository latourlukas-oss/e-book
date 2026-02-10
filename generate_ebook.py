import base64
import os

# Read base64 encoded images
def read_b64(path):
    with open(path, 'r') as f:
        return f.read().strip()

mining_photo = read_b64('/tmp/mining.b64')
confined1 = read_b64('/tmp/confined1.b64')
confined2 = read_b64('/tmp/confined2.b64')
sentry = read_b64('/tmp/sentry.b64')
heights1 = read_b64('/tmp/heights1.b64')
scaff = read_b64('/tmp/scaff.b64')
traffic = read_b64('/tmp/traffic.b64')
rope1 = read_b64('/tmp/rope1.b64')
rope2 = read_b64('/tmp/rope2.b64')
weld = read_b64('/tmp/weld.b64')
oil1 = read_b64('/tmp/oil1.b64')
oil2 = read_b64('/tmp/oil2.b64')

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Ultimate Working Holiday Guide to Australia</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        :root {{
            --green: #22c55e;
            --yellow: #eab308;
            --brown: #a16207;
            --blue: #3b82f6;
            --dark: #1e293b;
            --light: #f8fafc;
        }}
        
        body {{
            font-family: 'Inter', sans-serif;
            line-height: 1.6;
            color: #1e293b;
            background: #f8fafc;
        }}
        
        .page {{
            width: 210mm;
            min-height: 297mm;
            margin: 0 auto;
            background: white;
            padding: 15mm 20mm;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            page-break-after: always;
            position: relative;
        }}
        
        .cover {{
            background: linear-gradient(135deg, #1e3a5f 0%, #0f172a 100%);
            color: white;
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 20mm;
        }}
        
        .cover h1 {{
            font-size: 32px;
            font-weight: 800;
            margin-bottom: 15px;
            letter-spacing: 2px;
        }}
        
        .cover .subtitle {{
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 3px;
            color: #94a3b8;
            margin-bottom: 30px;
        }}
        
        .cover-photo {{
            width: 180px;
            height: 180px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid #3b82f6;
            margin: 20px 0;
        }}
        
        .flag {{
            font-size: 48px;
            margin-bottom: 20px;
        }}
        
        h2 {{
            font-size: 22px;
            color: #1e3a5f;
            margin: 20px 0 15px;
            padding-bottom: 8px;
            border-bottom: 3px solid #3b82f6;
        }}
        
        h3 {{
            font-size: 18px;
            color: #1e3a5f;
            margin: 15px 0 10px;
        }}
        
        h4 {{
            font-size: 15px;
            color: #334155;
            margin: 12px 0 8px;
        }}
        
        p {{
            margin-bottom: 10px;
            font-size: 11px;
        }}
        
        .tier-badge {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-weight: 600;
            font-size: 10px;
            margin-right: 10px;
        }}
        
        .tier-green {{ background: #dcfce7; color: #166534; }}
        .tier-yellow {{ background: #fef9c3; color: #854d0e; }}
        .tier-brown {{ background: #fef3c7; color: #92400e; }}
        .tier-blue {{ background: #dbeafe; color: #1e40af; }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 10px 0;
            font-size: 10px;
        }}
        
        th, td {{
            padding: 8px 10px;
            text-align: left;
            border: 1px solid #e2e8f0;
        }}
        
        th {{
            background: #f1f5f9;
            font-weight: 600;
            color: #334155;
        }}
        
        tr:nth-child(even) {{ background: #f8fafc; }}
        
        .info-box {{
            background: #eff6ff;
            border-left: 4px solid #3b82f6;
            padding: 12px 15px;
            margin: 15px 0;
            border-radius: 0 8px 8px 0;
            font-size: 11px;
        }}
        
        .warning-box {{
            background: #fef3c7;
            border-left: 4px solid #f59e0b;
            padding: 12px 15px;
            margin: 15px 0;
            border-radius: 0 8px 8px 0;
            font-size: 11px;
        }}
        
        .success-box {{
            background: #dcfce7;
            border-left: 4px solid #22c55e;
            padding: 12px 15px;
            margin: 15px 0;
            border-radius: 0 8px 8px 0;
            font-size: 11px;
        }}
        
        .pro-hack {{
            background: linear-gradient(135deg, #7c3aed 0%, #4f46e5 100%);
            color: white;
            padding: 20px;
            border-radius: 12px;
            margin: 20px 0;
        }}
        
        .pro-hack h3 {{
            color: #fbbf24;
            margin-top: 0;
        }}
        
        .pay-highlight {{
            background: linear-gradient(135deg, #059669 0%, #047857 100%);
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
            margin: 10px 0;
            font-size: 12px;
        }}
        
        .image-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin: 15px 0;
        }}
        
        .image-grid img {{
            width: 100%;
            height: 120px;
            object-fit: cover;
            border-radius: 8px;
        }}
        
        .image-caption {{
            font-size: 9px;
            color: #64748b;
            text-align: center;
            margin-top: 4px;
        }}
        
        .single-image {{
            width: 100%;
            max-height: 180px;
            object-fit: cover;
            border-radius: 8px;
            margin: 10px 0;
        }}
        
        .glossary-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
            font-size: 9px;
        }}
        
        .glossary-item {{
            background: #f8fafc;
            padding: 6px 10px;
            border-radius: 4px;
            border-left: 3px solid #3b82f6;
        }}
        
        .glossary-item strong {{
            color: #1e3a5f;
            display: block;
            font-size: 10px;
        }}
        
        ul {{
            margin-left: 20px;
            margin-bottom: 10px;
            font-size: 11px;
        }}
        
        li {{
            margin-bottom: 5px;
        }}
        
        .stat-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            margin: 15px 0;
        }}
        
        .stat-box {{
            text-align: center;
            padding: 10px;
            background: #f1f5f9;
            border-radius: 8px;
        }}
        
        .stat-box .number {{
            font-size: 20px;
            font-weight: 700;
            color: #1e3a5f;
        }}
        
        .stat-box .label {{
            font-size: 9px;
            color: #64748b;
        }}
        
        .timeline {{
            margin: 15px 0;
        }}
        
        .timeline-item {{
            display: flex;
            align-items: flex-start;
            margin-bottom: 10px;
        }}
        
        .timeline-number {{
            width: 28px;
            height: 28px;
            background: #3b82f6;
            color: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            font-size: 12px;
            margin-right: 12px;
            flex-shrink: 0;
        }}
        
        .timeline-content {{
            flex: 1;
            font-size: 11px;
        }}
        
        @media print {{
            body {{ background: white; }}
            .page {{
                box-shadow: none;
                margin: 0;
                page-break-after: always;
            }}
        }}
    </style>
</head>
<body>

<!-- PAGE 1: COVER -->
<div class="page cover">
    <div class="flag">🇦🇺</div>
    <h1>THE ULTIMATE WORKING HOLIDAY GUIDE TO AUSTRALIA</h1>
    <p class="subtitle">A Non Bullshit Approach on How to Succeed as a Backpacker in Australia</p>
    <img src="data:image/jpeg;base64,{mining_photo}" class="cover-photo" alt="Author">
    <p style="font-size: 12px; margin-top: 20px;">A Systematic Guide for Securing a Job — Everything Discussed from Farming, Construction, Mining and Oil & Gas</p>
    <p style="font-size: 14px; margin-top: 30px; color: #60a5fa;">From Backpacker to $200K Mining Professional — A 13-Year Journey</p>
</div>

<!-- PAGE 2: PRO HACK - CONSTRUCTION TRAINING FUND -->
<div class="page">
    <div class="pro-hack">
        <h3>💰 PRO HACK: Get Your Tickets REIMBURSED!</h3>
        <p style="font-size: 13px; margin-top: 10px;">Before spending thousands on tickets, read this — you could save up to $3,000!</p>
    </div>
    
    <h2>🎫 Construction Training Fund — Your Secret Weapon</h2>
    
    <p>One of the biggest mistakes backpackers make is paying full price for their tickets. What many don't know is that <strong>state-funded Construction Training Funds</strong> exist to subsidize your training costs!</p>
    
    <div class="success-box">
        <strong>💡 Real Savings Example:</strong><br>
        Intermediate Rigging Course: $1,500 → After subsidy: ~$500-800<br>
        Working at Heights + Confined Space: $600 → After subsidy: ~$200-300<br>
        <strong>Total potential savings: Up to $3,000 per year!</strong>
    </div>
    
    <h3>What is the Construction Training Fund?</h3>
    <p>Each Australian state has a training fund or authority that provides subsidies for construction and mining-related training. These funds collect levies from construction projects and redistribute them as training subsidies for workers in the industry.</p>
    
    <h3>How to Get Your Tickets Reimbursed</h3>
    
    <div class="timeline">
        <div class="timeline-item">
            <div class="timeline-number">1</div>
            <div class="timeline-content">
                <strong>Get Your CITB/Training Number (FREE)</strong><br>
                Apply online through your state's training authority. Takes 5-10 minutes. No cost.
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-number">2</div>
            <div class="timeline-content">
                <strong>Choose an Approved Training Provider</strong><br>
                Ensure your RTO is registered with the training fund. Most major providers are.
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-number">3</div>
            <div class="timeline-content">
                <strong>Provide Your Number at Enrollment</strong><br>
                Give your CITB number when booking your course. Critical step!
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-number">4</div>
            <div class="timeline-content">
                <strong>Subsidy Applied Automatically</strong><br>
                The discount is applied directly — you pay the reduced rate upfront.
            </div>
        </div>
    </div>
    
    <h3>State Training Authorities</h3>
    <table>
        <tr><th>State</th><th>Authority</th><th>Website</th></tr>
        <tr><td>South Australia</td><td>CITB</td><td>citb.org.au</td></tr>
        <tr><td>Western Australia</td><td>Jobs and Skills WA</td><td>jobsandskills.wa.gov.au</td></tr>
        <tr><td>Queensland</td><td>Construction Skills QLD</td><td>csq.org.au</td></tr>
        <tr><td>New South Wales</td><td>Training Services NSW</td><td>training.nsw.gov.au</td></tr>
        <tr><td>Victoria</td><td>Skills Victoria</td><td>skills.vic.gov.au</td></tr>
    </table>
    
    <h3>Tickets Eligible for Subsidies</h3>
    <ul>
        <li><strong>High Risk Work Licences:</strong> Rigging, Scaffolding, Forklift, Dogging</li>
        <li><strong>Safety Tickets:</strong> Working at Heights, Confined Space, EWP</li>
        <li><strong>Trade Courses:</strong> Welding certifications, First Aid, Traffic Control</li>
        <li><strong>Mining Inductions:</strong> Standard 11 (some states)</li>
    </ul>
    
    <div class="warning-box">
        <strong>⚠️ Important Tips:</strong>
        <ul style="margin-top: 8px; margin-bottom: 0;">
            <li>Apply for your training number BEFORE booking courses</li>
            <li>Not all RTOs participate — confirm before enrolling</li>
            <li>Keep receipts even if subsidy is applied (for tax purposes)</li>
            <li>Some subsidies require you to be working in construction</li>
        </ul>
    </div>
</div>

<!-- PAGE 3: TICKETS PAGE (preserved from original) -->
<div class="page">
    <h2>📜 My Tickets & Certifications</h2>
    <p style="font-style: italic; color: #64748b;">Personal information redacted for privacy</p>
    
    <h2>📊 Job Tier Color-Coding System</h2>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 20px 0;">
        <div style="background: #dcfce7; padding: 15px; border-radius: 8px;">
            <strong style="color: #166534;">🟢 GREEN: Entry-Level Jobs</strong><br>
            <span style="font-size: 11px;">$20-35/hr — Hospitality, Farm Work</span>
        </div>
        <div style="background: #fef9c3; padding: 15px; border-radius: 8px;">
            <strong style="color: #854d0e;">🟡 YELLOW: Mid-Tier Jobs</strong><br>
            <span style="font-size: 11px;">$45-65/hr — Mining Labourer, Rigging</span>
        </div>
        <div style="background: #fef3c7; padding: 15px; border-radius: 8px;">
            <strong style="color: #92400e;">🟤 BROWN: Trade Jobs</strong><br>
            <span style="font-size: 11px;">$55-80/hr — Boilermaker, Fitter</span>
        </div>
        <div style="background: #dbeafe; padding: 15px; border-radius: 8px;">
            <strong style="color: #1e40af;">🔵 BLUE: Mining & Senior Roles</strong><br>
            <span style="font-size: 11px;">$65-110+/hr — Operators, Specialists</span>
        </div>
    </div>
</div>

<!-- PAGE 4: TABLE OF CONTENTS -->
<div class="page">
    <h2>📑 Table of Contents</h2>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px;">
        <div>
            <h4>Part 1: Essential Foundations</h4>
            <ul>
                <li>Construction Training Fund (PRO HACK)</li>
                <li>Understanding FIFO</li>
                <li>Tier 1: Entry-Level Jobs</li>
                <li>Tier 2: Seasonal Farm Work</li>
                <li>Tier 3: Construction Work</li>
                <li>Rigging & Scaffolding Careers</li>
                <li>High Risk Work Licences</li>
                <li>Tier 4: Mining Labourer</li>
            </ul>
        </div>
        <div>
            <h4>Trade Careers & Beyond</h4>
            <ul>
                <li>Trade Assistant Roles</li>
                <li>Working at Heights & Confined Spaces</li>
                <li>Tier 5: Mining Operators</li>
                <li>Tier 6: Senior Roles</li>
                <li>RPL: Fast-Track Qualification</li>
                <li>TAFE Courses</li>
                <li>Oil & Gas Offshore</li>
            </ul>
        </div>
    </div>
</div>

<!-- PAGE 5: GLOSSARY (Updated with new terms) -->
<div class="page">
    <h2>📖 Glossary of Terms</h2>
    <p style="font-size: 10px; color: #64748b; margin-bottom: 15px;">Essential terminology for working in Australian construction, mining, and trades</p>
    
    <div class="glossary-grid">
        <div class="glossary-item">
            <strong>FIFO</strong>
            Fly-In Fly-Out work arrangement where workers fly to remote sites for set rosters
        </div>
        <div class="glossary-item">
            <strong>DIDO</strong>
            Drive-In Drive-Out — similar to FIFO but workers drive instead of fly
        </div>
        <div class="glossary-item">
            <strong>RTO</strong>
            Registered Training Organization — accredited training provider
        </div>
        <div class="glossary-item">
            <strong>HRW</strong>
            High Risk Work Licence — nationally recognized credential for dangerous work
        </div>
        <div class="glossary-item">
            <strong>VOC</strong>
            Verification of Competency — site-specific equipment assessment
        </div>
        <div class="glossary-item">
            <strong>Standard 11</strong>
            Underground mining general induction certificate
        </div>
        <div class="glossary-item">
            <strong>EWP</strong>
            Elevated Work Platform — scissor lifts, boom lifts
        </div>
        <div class="glossary-item">
            <strong>RPL</strong>
            Recognition of Prior Learning — converting experience to qualifications
        </div>
        <div class="glossary-item">
            <strong>White Card</strong>
            General construction induction card required for all sites
        </div>
        <div class="glossary-item">
            <strong>Shutdown</strong>
            Intensive maintenance period at mines/plants requiring many workers
        </div>
        <div class="glossary-item">
            <strong>BOSIET</strong>
            Basic Offshore Safety Induction & Emergency Training for oil & gas
        </div>
        <div class="glossary-item">
            <strong>MSIC</strong>
            Maritime Security Identification Card for offshore work
        </div>
        <div class="glossary-item">
            <strong>AS1796</strong>
            Australian welding certification standard
        </div>
        <div class="glossary-item">
            <strong>CITB</strong>
            Construction Industry Training Board — provides training subsidies
        </div>
        <div class="glossary-item">
            <strong>Confined Space</strong>
            Enclosed/partially enclosed space not designed for continuous occupancy
        </div>
        <div class="glossary-item">
            <strong>Confined Space Sentry Officer</strong>
            Person monitoring workers in confined spaces, maintaining communication
        </div>
        <div class="glossary-item">
            <strong>Gas Testing</strong>
            Testing atmosphere in confined spaces for oxygen, toxic & flammable gases
        </div>
        <div class="glossary-item">
            <strong>Spotters</strong>
            Safety personnel who monitor workers at heights or near hazards
        </div>
        <div class="glossary-item">
            <strong>Working at Heights</strong>
            Work where a person could fall and injure themselves (typically 2m+)
        </div>
        <div class="glossary-item">
            <strong>Rope Access</strong>
            Industrial technique using ropes to access difficult locations
        </div>
        <div class="glossary-item">
            <strong>IRATA</strong>
            Industrial Rope Access Trade Association — international rope certification
        </div>
        <div class="glossary-item">
            <strong>TIG/MIG Welding</strong>
            Tungsten/Metal Inert Gas welding processes
        </div>
        <div class="glossary-item">
            <strong>Dogging</strong>
            Entry-level rigging — directing crane operators, slinging loads
        </div>
        <div class="glossary-item">
            <strong>Roustabout</strong>
            Entry-level general labourer on offshore oil/gas platforms
        </div>
    </div>
</div>

<!-- PAGE 6: FOREWORD -->
<div class="page">
    <h2>Foreword</h2>
    <p>This guide provides maximum value for those pursuing working holiday opportunities in Australia. Based on 13+ years of personal experience, it covers farming, construction, hospitality, and mining sectors — with recommendations tailored to your work history, intended stay duration, and budget.</p>
    
    <div class="info-box">
        <em>"Wise people learn from other people's mistakes. I encourage you to learn from mine so you can avoid unnecessary suffering and bad financial decisions."</em>
    </div>
    
    <h2>Part 1: Essential Foundations</h2>
    
    <h3>Understanding Australian Working Holiday Visas</h3>
    <table>
        <tr><th>Visa Type</th><th>Subclass</th><th>Eligible Countries</th></tr>
        <tr><td>Working Holiday visa</td><td>417</td><td>UK, Ireland, Canada, Germany, France, others</td></tr>
        <tr><td>Work and Holiday visa</td><td>462</td><td>USA, Argentina, Chile, Indonesia, Vietnam, others</td></tr>
    </table>
    
    <h4>Basic Requirements</h4>
    <ul>
        <li>Age: 18-30 years (some nationalities up to 35)</li>
        <li>Eligible passport with no dependent children</li>
        <li>Minimum funds: AUD $5,000</li>
        <li>Must be outside Australia when applying for first visa</li>
        <li>Meet health and character requirements</li>
    </ul>
    
    <h4>Application Process</h4>
    <ol style="margin-left: 20px; font-size: 11px;">
        <li>Create an ImmiAccount through the Australian Government immigration website</li>
        <li>Start new visa application and select correct subclass</li>
        <li>Fill in personal details, passport info, travel history</li>
        <li>Upload documents (passport copy; 462 may need education proof)</li>
        <li>Pay application fee — AUD $635</li>
        <li>Wait for decision — many approved within minutes</li>
    </ol>
    
    <div class="success-box">
        <strong>Extending Your Stay:</strong>
        <ul style="margin-top: 8px; margin-bottom: 0;">
            <li>Second visa: Complete 3 months of specified work in regional areas</li>
            <li>Third visa: Complete 6 months of specified work on your second visa</li>
            <li>Total potential stay: Up to 3 years</li>
        </ul>
    </div>
    
    <h3>Tax File Number (TFN)</h3>
    <p>Apply online through the ATO website once you arrive in Australia with a valid visa (417, 462, student, etc.).</p>
</div>

<!-- PAGE 7: CAR & AGENCIES -->
<div class="page">
    <h2>🚗 Why a Car is Your Best Investment</h2>
    <ul>
        <li>Public transport in Australia is limited and unreliable</li>
        <li>Cars hold their value well</li>
        <li>Avoid expensive hostel traps ($300+/week for shared dorms)</li>
        <li>One week without work can cost $2,000+ AUD</li>
    </ul>
    
    <table>
        <tr><th>Budget Range</th><th>Vehicle Options</th></tr>
        <tr><td>$2,000-$7,000</td><td>Great Wall 4x4, Honda CR-V, Mitsubishi ASX, RAV4</td></tr>
        <tr><td>$8,000-$15,000</td><td>Pajero, Kluger, Pathfinder, Navara/Triton utes</td></tr>
        <tr><td>$15,000+</td><td>Toyota Hilux, Land Cruiser Prado</td></tr>
    </table>
    
    <div class="success-box">
        <strong>Success Story:</strong> "I bought an 80-series Landcruiser at 377,000 km for $11,000 and sold it at 417,000 km for $14,000."
    </div>
    
    <h2>Understanding Recruitment Agencies</h2>
    <p>Used for construction, mining, and farming. Agency charges client more than they pay you (margin = profit). Example: Agency charges $70/hr, pays you $40/hr = $30/hr profit.</p>
    
    <div class="warning-box">
        <strong>⚠️ Key Points:</strong> You'll mostly work on casual basis with no paid sick days or holiday pay. Avoid Gumtree jobs — often cash-in-hand with no insurance.
    </div>
    
    <h2>Mastering the Job Search</h2>
    <div class="info-box">
        <em>"Think of sending your resume like planting a seed. Then water it by calling when you don't hear back. Call at least once a week. Hearing back can take up to 3 months."</em>
    </div>
    
    <h4>How to Call Recruitment Agencies</h4>
    <ol style="margin-left: 20px; font-size: 11px;">
        <li>Be calm — don't rush or sound desperate</li>
        <li>Start with small talk — "Hey, how are you going?"</li>
        <li>Be specific — state your name and exact job you want</li>
        <li>Follow up — this sets you apart from others</li>
    </ol>
</div>

<!-- PAGE 8: FIFO -->
<div class="page">
    <h2>🛩️ Understanding FIFO (Fly-In Fly-Out)</h2>
    
    <h3>What is FIFO?</h3>
    <p>FIFO is a work arrangement common in Australian mining. Workers fly from their home city to a remote mine site, work a set roster (typically 2 weeks on, 1 week off), then fly home.</p>
    
    <h4>What's Included:</h4>
    <ul>
        <li>✈️ Flights: Employer pays all flights</li>
        <li>🏠 Accommodation: Purpose-built mining camps — FREE</li>
        <li>🍽️ Meals: All meals provided in camp mess — FREE</li>
        <li>🚐 Transport: Bus transfers — FREE</li>
        <li>📶 Facilities: Gym, recreation room, WiFi, laundry</li>
    </ul>
    
    <h2>💰 The Savings Advantage of Living on Camp</h2>
    <p><strong>Why FIFO = Maximum Savings:</strong> While on camp, you have virtually ZERO living expenses!</p>
    
    <table>
        <tr><th>Expense</th><th>City Living</th><th>FIFO Camp</th></tr>
        <tr><td>Rent/Accommodation</td><td>$1,600-$2,500</td><td>$0</td></tr>
        <tr><td>Food/Groceries</td><td>$600-$1,000</td><td>$0</td></tr>
        <tr><td>Utilities</td><td>$200-$400</td><td>$0</td></tr>
        <tr><td>Transport/Fuel</td><td>$300-$600</td><td>$0</td></tr>
        <tr><td><strong>TOTAL</strong></td><td><strong>$2,700-$4,500</strong></td><td><strong>$0!</strong></td></tr>
    </table>
    
    <div class="success-box">
        <strong>Real Example:</strong> Mining Labourer earning $48/hr on a 2:1 roster:<br>
        Weekly earnings on site: ~$4,000+ (with overtime)<br>
        Monthly gross: ~$8,000-$10,000<br>
        <strong>Potential annual savings: $80,000-$100,000+</strong>
    </div>
    
    <h3>Common FIFO Rosters</h3>
    <table>
        <tr><th>Roster</th><th>Days On</th><th>Days Off</th><th>Best For</th></tr>
        <tr><td>2:1</td><td>14</td><td>7</td><td>Most common, good balance</td></tr>
        <tr><td>8:6</td><td>8</td><td>6</td><td>Better work-life balance</td></tr>
        <tr><td>4:3</td><td>4</td><td>3</td><td>DIDO roles</td></tr>
        <tr><td>15:13</td><td>15</td><td>13</td><td>Senior/specialist roles</td></tr>
    </table>
</div>

<!-- PAGE 9: TIER 1 -->
<div class="page">
    <h2><span class="tier-badge tier-green">🟢 TIER 1</span> Entry-Level Jobs ($20-$28/hour)</h2>
    
    <h3>1.1 Hospitality — Housekeeping & Cleaning</h3>
    <p>Entry-level cleaning and housekeeping roles in hotels, hostels, and resorts.</p>
    
    <div class="pay-highlight">
        Pay: $22-$28/hr | Weekly: $880-$1,120 | Annual: $45,000-$58,000
    </div>
    
    <table>
        <tr><th>Requirement</th><th>Cost</th><th>Notes</th></tr>
        <tr><td>None mandatory</td><td>$0</td><td>Basic entry-level position</td></tr>
        <tr><td>RSA (optional)</td><td>$60-$150</td><td>Beneficial if role includes bar areas</td></tr>
    </table>
    
    <div class="warning-box">
        <strong>⚠️ Warning:</strong> Avoid businesses offering unpaid trial days — this is illegal in Australia!
    </div>
    
    <h3>1.2 Hospitality — Restaurant & Café Work</h3>
    <p>Food service roles including waiting tables, food prep, barista work, and kitchen hand duties.</p>
    
    <div class="pay-highlight">
        Pay: $23-$30/hr (casual) | Weekly: $920-$1,200 | Annual: $48,000-$62,000
    </div>
    
    <table>
        <tr><th>Requirement</th><th>Cost</th><th>Validity</th></tr>
        <tr><td>RSA (Responsible Service of Alcohol)</td><td>$60-$150</td><td>State-specific, 3-5 years</td></tr>
        <tr><td>Food Safety Certificate</td><td>$80-$150</td><td>Varies by state</td></tr>
    </table>
</div>

<!-- PAGE 10: TIER 2 -->
<div class="page">
    <h2><span class="tier-badge tier-green">🟢 TIER 2</span> Seasonal Farm Work ($25-$40/hour)</h2>
    
    <h3>2.1 Tractor Driving / Farm Hand ✅ RECOMMENDED</h3>
    <p>Operating tractors with GPS auto-steer systems for seeding, harvesting, and general farm operations.</p>
    
    <div class="pay-highlight">
        Pay: $28-$40/hr | Weekly (50-60 hrs): $1,400-$2,400 | Seasonal: $15,000-$20,000+ saved
    </div>
    
    <div class="success-box">
        <strong>Real Example:</strong> "I saved around $17,000 in four months driving a tractor."
    </div>
    
    <table>
        <tr><th>Requirement</th><th>Cost</th><th>Notes</th></tr>
        <tr><td>None required</td><td>$0</td><td>Farmland is private — no licenses needed</td></tr>
        <tr><td>First Aid (optional)</td><td>$100-$150</td><td>Some farms prefer this</td></tr>
    </table>
    
    <h4>Seeding Seasons:</h4>
    <table>
        <tr><th>Crop Type</th><th>Season</th><th>Regions</th></tr>
        <tr><td>Winter crops</td><td>April-June</td><td>WA, SA, VIC, NSW</td></tr>
        <tr><td>Summer crops</td><td>Sept-Dec</td><td>Northern NSW, QLD</td></tr>
    </table>
    
    <div class="info-box">
        <strong>Key Benefits:</strong> ✅ Food & accommodation usually supplied | ✅ Counts towards 88 days for visa | ✅ No experience necessary | ✅ No licenses needed
    </div>
    
    <h3>2.2 Fruit Picking ❌ NOT RECOMMENDED</h3>
    <div class="warning-box">
        <strong>⚠️ AVOID:</strong>
        <ul style="margin-top: 8px; margin-bottom: 0;">
            <li>Paid by piece rate — often $15-$25/hour effective</li>
            <li>"Working hostels" overcharge for accommodation</li>
            <li>Exposure to pesticides causing rashes</li>
            <li>Inconsistent work (sent home when it rains)</li>
        </ul>
    </div>
</div>

<!-- PAGE 11: TIER 3 - CONSTRUCTION -->
<div class="page">
    <h2><span class="tier-badge tier-green">🟢 TIER 3</span> Construction Work ($35-$50/hour)</h2>
    
    <h3>3.1 Construction Labourer</h3>
    <p>General labouring including material handling, site cleanup, basic trades assistance, and operating small equipment.</p>
    
    <div class="pay-highlight">
        Pay: $35-$45/hr | Daily: $350-$450 | Weekly: $1,750-$2,250 | Annual: $85,000-$115,000
    </div>
    
    <div class="success-box">
        <strong>Real Example:</strong> "My French friends earned $400 a day each for a couple of months in construction outside the city."
    </div>
    
    <h4>Required Tickets:</h4>
    <table>
        <tr><th>Requirement</th><th>Cost</th><th>Validity</th></tr>
        <tr><td>White Card (Construction Induction)</td><td>$80-$150</td><td>No expiry</td></tr>
        <tr><td>Standard Driver's License</td><td>—</td><td>Varies</td></tr>
        <tr><td>Manual Handling Certificate</td><td>$80-$120</td><td>3 years</td></tr>
    </table>
    
    <h4>Optional But Valuable:</h4>
    <table>
        <tr><th>Ticket</th><th>Cost</th><th>Benefit</th></tr>
        <tr><td>Working at Heights</td><td>$200-$350</td><td>More job opportunities</td></tr>
        <tr><td>EWP (Elevated Work Platform)</td><td>$250-$400</td><td>Operate scissor/boom lifts</td></tr>
        <tr><td>Forklift License (LF)</td><td>$250-$400</td><td>Warehouse/site work</td></tr>
    </table>
    
    <h3>3.2 Traffic Controller</h3>
    <div class="pay-highlight">
        Pay: $35-$50/hr | Daily: $350-$500 | Weekly: $1,750-$2,500 | Annual: $80,000-$120,000
    </div>
    
    <img src="data:image/jpeg;base64,{traffic}" class="single-image" alt="Traffic Controller at work site">
    <p class="image-caption">Traffic controllers managing site access — a popular entry point into construction</p>
    
    <table>
        <tr><th>Requirement</th><th>Cost</th><th>Validity</th></tr>
        <tr><td>Traffic Controller Ticket</td><td>$250-$400</td><td>3 years</td></tr>
        <tr><td>White Card</td><td>$80-$150</td><td>No expiry</td></tr>
        <tr><td>First Aid Certificate</td><td>$100-$150</td><td>3 years</td></tr>
    </table>
</div>

<!-- PAGE 12: RIGGING & SCAFFOLDING -->
<div class="page">
    <h2><span class="tier-badge tier-yellow">🟡</span> Rigging & Scaffolding Careers ($45-$65/hour)</h2>
    <p>High-demand mid-tier roles across mining, construction, and oil & gas sectors.</p>
    
    <h3>🔧 Rigging Career Levels</h3>
    <p>Riggers safely move heavy loads using cranes, hoists, and lifting equipment.</p>
    
    <table>
        <tr><th>Level</th><th>Description</th><th>Pay</th></tr>
        <tr><td>Dogging</td><td>Entry-level: directing crane operators, loads up to 20t</td><td>$40-$50/hr</td></tr>
        <tr><td>Basic Rigging</td><td>Equipment setup, structural steel erection</td><td>$45-$55/hr</td></tr>
        <tr><td>Intermediate</td><td>Multi-crane lifts, complex load calculations</td><td>$55-$65/hr</td></tr>
        <tr><td>Advanced</td><td>Heavy machinery, structures over 20t</td><td>$60-$75/hr</td></tr>
    </table>
    
    <h3>🏗️ Scaffolding Career Levels</h3>
    <p>Scaffolders erect, alter, and dismantle temporary work platforms.</p>
    
    <table>
        <tr><th>Level</th><th>Description</th><th>Pay</th></tr>
        <tr><td>Basic</td><td>Prefab modular scaffolds, restricted heights</td><td>$40-$50/hr</td></tr>
        <tr><td>Intermediate</td><td>Modular and tube scaffolds</td><td>$50-$60/hr</td></tr>
        <tr><td>Advanced</td><td>Hung/suspended scaffolds, complex structures</td><td>$55-$70/hr</td></tr>
    </table>
    
    <div class="success-box">
        <strong>💰 Annual Potential:</strong><br>
        Intermediate Rigger (FIFO): $120,000-$150,000/year<br>
        Advanced Scaffolder (Shutdown): $130,000-$160,000/year
    </div>
    
    <h4>Career Progression:</h4>
    <div class="timeline">
        <div class="timeline-item">
            <div class="timeline-number">1</div>
            <div class="timeline-content"><strong>Start:</strong> Trade Assistant/Labourer — Get White Card</div>
        </div>
        <div class="timeline-item">
            <div class="timeline-number">2</div>
            <div class="timeline-content"><strong>Get Licensed:</strong> Basic/Intermediate HRW Licence (1-2 weeks)</div>
        </div>
        <div class="timeline-item">
            <div class="timeline-number">3</div>
            <div class="timeline-content"><strong>Gain Experience:</strong> 6-12 months site experience</div>
        </div>
        <div class="timeline-item">
            <div class="timeline-number">4</div>
            <div class="timeline-content"><strong>Advanced:</strong> Mining FIFO or Shutdown Work — $60-$75/hr</div>
        </div>
    </div>
</div>

<!-- PAGE 13: HRW LICENCES -->
<div class="page">
    <h2>📋 High Risk Work Licences (HRW)</h2>
    <p>Nationally recognized credentials required by law for specific high-risk activities.</p>
    
    <h3>Types of HRW Licences</h3>
    <table>
        <tr><th>Class</th><th>Description</th><th>Cost</th><th>Duration</th></tr>
        <tr><td>DG</td><td>Dogging</td><td>$800-$1,200</td><td>3-5 days</td></tr>
        <tr><td>RB</td><td>Basic Rigging</td><td>$1,000-$1,500</td><td>5 days</td></tr>
        <tr><td>RI</td><td>Intermediate Rigging</td><td>$1,200-$1,800</td><td>5-7 days</td></tr>
        <tr><td>RA</td><td>Advanced Rigging</td><td>$1,500-$2,500</td><td>5-7 days</td></tr>
        <tr><td>SB</td><td>Basic Scaffolding</td><td>$800-$1,200</td><td>3-5 days</td></tr>
        <tr><td>SI</td><td>Intermediate Scaffolding</td><td>$1,000-$1,500</td><td>5 days</td></tr>
        <tr><td>LF</td><td>Forklift</td><td>$250-$400</td><td>1-2 days</td></tr>
        <tr><td>WP</td><td>Boom-type EWP</td><td>$300-$500</td><td>1-2 days</td></tr>
    </table>
    
    <div class="info-box">
        <strong>Why WA is Best for Getting Licensed:</strong>
        <ul style="margin-top: 8px; margin-bottom: 0;">
            <li>✅ More training providers = competitive prices</li>
            <li>✅ Mining companies often pay for tickets once employed</li>
            <li>✅ Immediate job opportunities</li>
            <li>✅ Construction Training Fund may reimburse costs</li>
        </ul>
    </div>
    
    <h4>Process to Get HRW Licence:</h4>
    <ol style="margin-left: 20px; font-size: 11px;">
        <li>Choose an RTO (TAFE WA, Nara Training, iCollege)</li>
        <li>Complete training course (theory + practical)</li>
        <li>Pass the assessment</li>
        <li>Apply to WorkSafe WA with your NOA</li>
        <li>Receive licence card — valid 5 years Australia-wide</li>
    </ol>
    
    <h4>Training Providers in WA:</h4>
    <table>
        <tr><th>Provider</th><th>Location</th><th>Speciality</th></tr>
        <tr><td>TAFE WA</td><td>Perth, Joondalup</td><td>Full range of HRW courses</td></tr>
        <tr><td>Nara Training</td><td>Perth, Kalgoorlie</td><td>Mining-focused</td></tr>
        <tr><td>iCollege</td><td>Perth</td><td>Construction tickets</td></tr>
        <tr><td>ERGT Australia</td><td>Perth</td><td>Oil & gas, mining safety</td></tr>
    </table>
</div>

<!-- PAGE 14: TIER 4 - MINING LABOURER -->
<div class="page">
    <h2><span class="tier-badge tier-yellow">🟡 TIER 4</span> Mining Labourer & Trade Assistant ($48-$55/hour)</h2>
    
    <h3>Mining Labourer / Trade Assistant</h3>
    <p>General support work including ventilation maintenance, pipe installation, equipment moving, ground support, and assisting tradespeople.</p>
    
    <div class="pay-highlight">
        Pay: $48-$55/hr (nights up to $60+/hr) | Daily: $576-$660 | Roster: 2:1<br>
        Annual: $110,000-$140,000
    </div>
    
    <h4>Required Tickets:</h4>
    <table>
        <tr><th>Requirement</th><th>Cost</th><th>Validity</th></tr>
        <tr><td>Standard 11 (Underground Induction)</td><td>$300-$500</td><td>5 years</td></tr>
        <tr><td>Working at Heights</td><td>$200-$350</td><td>2-5 years</td></tr>
        <tr><td>Confined Space</td><td>$250-$400</td><td>2-5 years</td></tr>
        <tr><td>First Aid</td><td>$100-$150</td><td>3 years</td></tr>
        <tr><td>Driver's License (C Class)</td><td>—</td><td>—</td></tr>
    </table>
    
    <h2>🏆 Why Western Australia for Mining</h2>
    <div class="stat-grid">
        <div class="stat-box">
            <div class="number">134,009</div>
            <div class="label">Mining Jobs in WA</div>
        </div>
        <div class="stat-box">
            <div class="number">47%</div>
            <div class="label">of AU Mining Workforce</div>
        </div>
        <div class="stat-box">
            <div class="number">11,065</div>
            <div class="label">New Workers by 2029</div>
        </div>
        <div class="stat-box">
            <div class="number">$200K+</div>
            <div class="label">Top Earner Potential</div>
        </div>
    </div>
    
    <div class="info-box">
        <strong>Why WA Dominates:</strong>
        <ul style="margin-top: 8px; margin-bottom: 0;">
            <li>🏆 Iron Ore Capital: 65,496 FTE jobs in Pilbara</li>
            <li>🥇 Gold Rush: 35,672 FTE jobs in Goldfields</li>
            <li>📈 40% of Australia's resource workforce growth</li>
            <li>🛠️ Critical skills shortage = easier to get hired</li>
            <li>✈️ Perth is the FIFO gateway</li>
        </ul>
    </div>
</div>

<!-- PAGE 15: NEW - WORKING AT HEIGHTS & CONFINED SPACES -->
<div class="page">
    <h2>🔒 Working at Heights & Confined Spaces</h2>
    <p style="color: #64748b; font-style: italic;">Essential certifications for Trade Assistants in Mining & Construction</p>
    
    <h3>⬆️ Working at Heights — Why It's Essential</h3>
    <p>Working at heights certification is <strong>mandatory for any work above 2 meters</strong> in Australian mining and construction. Due to strict safety regulations, falls from height are one of the most common causes of workplace fatalities.</p>
    
    <div class="image-grid">
        <div>
            <img src="data:image/jpeg;base64,{heights1}" alt="Working at heights in mining">
            <p class="image-caption">Scaffolding work in mining operations</p>
        </div>
        <div>
            <img src="data:image/jpeg;base64,{scaff}" alt="Scaffolding construction">
            <p class="image-caption">Professional scaffold erection</p>
        </div>
    </div>
    
    <h4>Why This Certification is Essential:</h4>
    <ul>
        <li><strong>Legal Requirement:</strong> Cannot work on elevated platforms without certification</li>
        <li><strong>Insurance Coverage:</strong> Uncertified work voids insurance</li>
        <li><strong>Higher Pay:</strong> Opens doors to scaffolding, rigging, and rope access roles</li>
        <li><strong>Site Access:</strong> Most mine sites require this ticket for ALL workers</li>
    </ul>
    
    <div class="info-box">
        <strong>🔍 SPOTTERS on Mine Sites</strong><br>
        Due to Australia's strict safety regulations, it's common for mine sites to employ <strong>SPOTTERS</strong> — dedicated safety personnel who monitor workers at heights. Their role includes:
        <ul style="margin-top: 8px; margin-bottom: 0;">
            <li>Observing workers for signs of fatigue or unsafe behavior</li>
            <li>Monitoring anchor points and fall arrest systems</li>
            <li>Coordinating emergency response if a fall occurs</li>
            <li>Ensuring exclusion zones are maintained below work areas</li>
        </ul>
    </div>
    
    <h4>Working at Heights Requirements:</h4>
    <table>
        <tr><th>Certification</th><th>Cost</th><th>Duration</th><th>Validity</th></tr>
        <tr><td>Working at Heights</td><td>$200-$350</td><td>1 day</td><td>2-5 years</td></tr>
        <tr><td>EWP (Boom/Scissor Lift)</td><td>$250-$400</td><td>1-2 days</td><td>5 years</td></tr>
        <tr><td>Basic Scaffolding (SB)</td><td>$800-$1,200</td><td>3-5 days</td><td>5 years</td></tr>
    </table>
</div>

<!-- PAGE 16: CONFINED SPACES -->
<div class="page">
    <h3>🚨 Confined Spaces — Critical for Mining</h3>
    <p>Confined space work is one of the <strong>highest-risk activities</strong> in mining. A confined space is any enclosed or partially enclosed space not designed for continuous human occupancy, with limited entry/exit points and potential for hazardous atmospheres.</p>
    
    <div class="image-grid">
        <div>
            <img src="data:image/jpeg;base64,{confined1}" alt="Confined space entry in mining">
            <p class="image-caption">Worker entering confined space with safety equipment</p>
        </div>
        <div>
            <img src="data:image/jpeg;base64,{confined2}" alt="Confined space work">
            <p class="image-caption">Industrial confined space operations</p>
        </div>
    </div>
    
    <h4>Why Confined Spaces Work is Essential in Mining:</h4>
    <ul>
        <li><strong>Underground Infrastructure:</strong> Tanks, silos, pits, shafts, and tunnels all require certified workers</li>
        <li><strong>Maintenance Critical:</strong> Regular inspections of vessels, pipes, and storage containers</li>
        <li><strong>High Demand:</strong> Every shutdown requires confined space certified workers</li>
        <li><strong>Premium Pay:</strong> Confined space work often pays 10-20% more</li>
    </ul>
    
    <div class="warning-box">
        <strong>⚠️ The Dangers of Confined Spaces:</strong>
        <ul style="margin-top: 8px; margin-bottom: 0;">
            <li>Oxygen deficiency (below 19.5%) — can cause unconsciousness in seconds</li>
            <li>Toxic gases (H2S, CO, methane) — often undetectable without equipment</li>
            <li>Engulfment hazards (grain, sand, liquids)</li>
            <li>Limited rescue access — specialized equipment required</li>
        </ul>
    </div>
    
    <h4>🔬 Gas Testing — The Most Critical Skill</h4>
    <p>Before ANY confined space entry, the atmosphere must be tested. This is non-negotiable.</p>
    
    <table>
        <tr><th>Gas</th><th>Safe Level</th><th>Danger</th></tr>
        <tr><td>Oxygen (O2)</td><td>19.5%-23.5%</td><td>Below 19.5% = asphyxiation risk</td></tr>
        <tr><td>Hydrogen Sulfide (H2S)</td><td>&lt;10 ppm</td><td>Highly toxic, "rotten egg" smell</td></tr>
        <tr><td>Carbon Monoxide (CO)</td><td>&lt;25 ppm</td><td>Odorless, causes confusion/death</td></tr>
        <tr><td>Lower Explosive Limit (LEL)</td><td>&lt;10%</td><td>Explosion/fire risk</td></tr>
    </table>
    
    <div class="info-box">
        <strong>Gas Testing Process:</strong>
        <ol style="margin-top: 8px; margin-bottom: 0;">
            <li>Test BEFORE entry — never assume the atmosphere is safe</li>
            <li>Test at multiple levels (top, middle, bottom) — gases stratify</li>
            <li>Continuous monitoring during work</li>
            <li>Calibrate equipment daily</li>
        </ol>
    </div>
</div>

<!-- PAGE 17: CONFINED SPACE SENTRY OFFICER -->
<div class="page">
    <h3>👤 NEW ROLE: Confined Space Sentry Officer</h3>
    <p>The <strong>Confined Space Sentry Officer</strong> (also called Standby Person or Hole Watch) is a critical safety role that monitors workers inside confined spaces.</p>
    
    <img src="data:image/jpeg;base64,{sentry}" class="single-image" alt="Confined Space Sentry Officer monitoring workers">
    <p class="image-caption">Confined Space Sentry Officer maintaining communication with workers below</p>
    
    <h4>Role & Responsibilities:</h4>
    <ul>
        <li><strong>Continuous Watch:</strong> Must remain at the entry point at ALL times</li>
        <li><strong>Communication:</strong> Maintain contact with workers inside (radio, visual, rope signals)</li>
        <li><strong>Emergency Response:</strong> Initiate rescue procedures if workers become distressed</li>
        <li><strong>Access Control:</strong> Ensure only authorized personnel enter</li>
        <li><strong>Monitoring:</strong> Track atmospheric conditions and time limits</li>
        <li><strong>Documentation:</strong> Log all entries, exits, and atmospheric readings</li>
    </ul>
    
    <div class="success-box">
        <strong>💡 Why This is a GREAT Entry Role:</strong>
        <ul style="margin-top: 8px; margin-bottom: 0;">
            <li>Lower physical demands than entry work</li>
            <li>Same hourly rate as confined space entrants</li>
            <li>Learn rescue procedures and gas testing</li>
            <li>Pathway to supervisor roles</li>
            <li>Always in demand during shutdowns</li>
        </ul>
    </div>
    
    <h4>Requirements to Become a Sentry Officer:</h4>
    <table>
        <tr><th>Requirement</th><th>Cost</th><th>Notes</th></tr>
        <tr><td>Confined Space Entry & Monitoring</td><td>$250-$400</td><td>Covers both entry and standby duties</td></tr>
        <tr><td>First Aid Certificate</td><td>$100-$150</td><td>Essential for emergency response</td></tr>
        <tr><td>Gas Testing Awareness</td><td>Included</td><td>Part of confined space course</td></tr>
        <tr><td>CPR/Low Voltage Rescue</td><td>$80-$150</td><td>Often required on mine sites</td></tr>
    </table>
    
    <div class="warning-box">
        <strong>⚠️ Critical Rule:</strong> The Sentry Officer must NEVER enter the confined space to attempt rescue. If a worker is in distress, they must immediately raise the alarm and initiate the emergency rescue procedure. Untrained rescuers often become additional victims.
    </div>
</div>

<!-- PAGE 18: SHUTDOWN WORK -->
<div class="page">
    <h2>⚡ Shutdown Work</h2>
    <p>Intensive maintenance periods requiring large numbers of workers for short contracts.</p>
    
    <div class="success-box">
        <strong>Why Shutdowns are GOLD for Backpackers:</strong>
        <ul style="margin-top: 8px; margin-bottom: 0;">
            <li>💰 Premium Pay: 10-20% higher rates</li>
            <li>📅 Flexible: 2-6 week contracts</li>
            <li>🔄 Year-Round: Different mines have different schedules</li>
            <li>🎓 Experience: Learn from experienced tradespeople</li>
        </ul>
    </div>
    
    <h4>Major WA Mining Regions:</h4>
    <table>
        <tr><th>Region</th><th>Commodities</th><th>Major Employers</th></tr>
        <tr><td>Pilbara</td><td>Iron Ore</td><td>BHP, Rio Tinto, FMG, Roy Hill</td></tr>
        <tr><td>Goldfields</td><td>Gold, Nickel</td><td>Northern Star, Evolution</td></tr>
        <tr><td>Mid West</td><td>Iron Ore, Gold</td><td>Karara Mining, Westgold</td></tr>
        <tr><td>South West</td><td>Alumina, Lithium</td><td>Alcoa, Talison Lithium</td></tr>
    </table>
    
    <h4>Finding Shutdown Work:</h4>
    <ul>
        <li><strong>Agencies:</strong> Programmed, Hays, Chandler Macleod, WorkPac</li>
        <li><strong>Job Boards:</strong> SEEK, Indeed</li>
        <li><strong>Direct:</strong> FMS Group, Premium Mechanical Group, Centurion</li>
    </ul>
</div>

<!-- PAGE 19: TRADE CAREERS -->
<div class="page">
    <h2><span class="tier-badge tier-brown">🟤</span> Trade Careers: Boilermaker & Fitter ($55-$80/hour)</h2>
    <p>The backbone of mining and construction — formal qualifications with exceptional earning potential.</p>
    
    <h3>Boilermaker</h3>
    <p>Fabricating, assembling, and repairing metal structures, tanks, pressure vessels, and heavy equipment.</p>
    
    <div class="pay-highlight">
        Pay: $55-$80/hr | Daily: $660-$960 | Annual (FIFO): $140,000-$180,000+
    </div>
    
    <table>
        <tr><th>Requirement</th><th>How to Get It</th></tr>
        <tr><td>Cert III Engineering - Fabrication Trade</td><td>Apprenticeship (3-4 yrs) OR RPL</td></tr>
        <tr><td>Welding Certifications (AS1796)</td><td>TAFE or RTO course</td></tr>
        <tr><td>Mine site tickets</td><td>Standard 11, Heights, Confined Space</td></tr>
    </table>
    
    <h3>Welding Work in Mining</h3>
    <div class="image-grid">
        <div>
            <img src="data:image/jpeg;base64,{weld}" alt="Professional welding work">
            <p class="image-caption">Precision welding on mining equipment</p>
        </div>
        <div>
            <img src="https://thumbs.dreamstime.com/b/side-view-industrial-rope-access-welder-maintenance-abseiler-wearing-fall-safety-body-safety-harness-helmet-protective-155554015.jpg" alt="Mining welder at work">
            <p class="image-caption">Rope access welder in mining operations</p>
        </div>
    </div>
    
    <h3>Fitter / Mechanical Fitter</h3>
    <p>Installing, maintaining, and repairing machinery and mechanical equipment.</p>
    
    <div class="pay-highlight">
        Pay: $55-$75/hr | Daily: $660-$900 | Annual (FIFO): $130,000-$170,000
    </div>
    
    <table>
        <tr><th>Requirement</th><th>How to Get It</th></tr>
        <tr><td>Cert III Engineering - Mechanical Trade</td><td>Apprenticeship (3-4 yrs) OR RPL</td></tr>
        <tr><td>Hydraulics knowledge</td><td>On-the-job or courses</td></tr>
        <tr><td>Mine site tickets</td><td>Standard 11, Heights, Confined Space</td></tr>
    </table>
</div>

<!-- PAGE 20: ROPE ACCESS -->
<div class="page">
    <h2>🧗 Rope Access — High-Demand Specialty</h2>
    <p>Industrial rope access technicians use specialized climbing techniques to access difficult locations for inspection, maintenance, and repair work.</p>
    
    <div class="image-grid">
        <div>
            <img src="data:image/jpeg;base64,{rope1}" alt="Rope access technician">
            <p class="image-caption">IRATA-certified rope access technician</p>
        </div>
        <div>
            <img src="data:image/jpeg;base64,{rope2}" alt="Rope access at height">
            <p class="image-caption">Industrial rope access work</p>
        </div>
    </div>
    
    <h4>Why Rope Access is Premium Work:</h4>
    <ul>
        <li><strong>Eliminates Scaffolding:</strong> Faster access = cost savings for clients</li>
        <li><strong>Specialized Skills:</strong> Limited supply of qualified technicians</li>
        <li><strong>Diverse Industries:</strong> Mining, oil & gas, wind turbines, buildings</li>
        <li><strong>International Recognition:</strong> IRATA certification valid worldwide</li>
    </ul>
    
    <div class="pay-highlight">
        IRATA Level 1: $45-$55/hr | Level 2: $55-$70/hr | Level 3: $70-$90/hr
    </div>
    
    <h4>IRATA Certification Pathway:</h4>
    <table>
        <tr><th>Level</th><th>Requirements</th><th>Cost</th><th>Duration</th></tr>
        <tr><td>Level 1</td><td>Basic fitness, no experience needed</td><td>$2,500-$3,500</td><td>5 days</td></tr>
        <tr><td>Level 2</td><td>1,000 logged hours as L1</td><td>$2,000-$2,500</td><td>5 days</td></tr>
        <tr><td>Level 3</td><td>1,000 logged hours as L2</td><td>$2,000-$2,500</td><td>5 days</td></tr>
    </table>
</div>

<!-- PAGE 21: TIER 5 -->
<div class="page">
    <h2><span class="tier-badge tier-blue">🔵 TIER 5</span> Mining — Experienced Operators ($65-$85/hour)</h2>
    
    <h3>Machinery Operator</h3>
    <p>Operating heavy machinery — dump trucks, loaders (CAT 996), excavators on surface or underground mines.</p>
    
    <div class="pay-highlight">
        Pay: $55-$75/hr | Daily: $660-$900 | Roster: 2:1 | Annual: $130,000-$170,000
    </div>
    
    <h4>Required Tickets:</h4>
    <table>
        <tr><th>Requirement</th><th>Cost</th><th>Notes</th></tr>
        <tr><td>HR License (Heavy Rigid)</td><td>$1,500-$3,000</td><td>Required for site driving</td></tr>
        <tr><td>Machinery VOCs</td><td>$400-$1,000 each</td><td>Site-specific assessments</td></tr>
        <tr><td>Standard 11 / Site Induction</td><td>$300-$500</td><td>5 years</td></tr>
    </table>
    
    <h4>Common Machinery VOCs:</h4>
    <table>
        <tr><th>Equipment</th><th>Cost</th></tr>
        <tr><td>Articulated Dump Truck (ADT)</td><td>$500-$1,000</td></tr>
        <tr><td>CAT 996 Loader</td><td>$500-$1,000</td></tr>
        <tr><td>Excavator</td><td>$500-$1,000</td></tr>
        <tr><td>Grader</td><td>$500-$1,000</td></tr>
        <tr><td>Water Cart</td><td>$300-$500</td></tr>
    </table>
</div>

<!-- PAGE 22: TIER 6 -->
<div class="page">
    <h2><span class="tier-badge tier-blue">🔵 TIER 6</span> Mining — Senior & Specialist ($85-$110+/hour)</h2>
    
    <h3>Mineral Process Operator</h3>
    <p>Safe processing of ore, fault-finding, communication with control room, SAP for maintenance scheduling.</p>
    
    <div class="pay-highlight">
        Pay: $70-$90/hr | Daily: $840-$1,080 | Roster: 15:13<br>
        Annual: $170,000-$210,000+
    </div>
    
    <div class="success-box">
        <strong>Real Example:</strong> "I currently work paying close to $200K per year on a 15-day-on, 13-day-off roster."
    </div>
    
    <h4>Requirements:</h4>
    <ul>
        <li>All Tier 4 & 5 tickets</li>
        <li>Process Plant Induction</li>
        <li>SAP/Maintenance Systems knowledge</li>
        <li>Dangerous Goods License ($200-$400)</li>
        <li>HR License (unrestricted)</li>
    </ul>
</div>

<!-- PAGE 23: RPL -->
<div class="page">
    <h2>🚀 RPL: Fast-Track to Trade Qualified</h2>
    
    <div class="info-box">
        <strong>What is RPL?</strong><br>
        RPL converts your existing work experience into a nationally recognized qualification — WITHOUT years of apprenticeship!<br><br>
        Think of it as getting credit for what you already know how to do.
    </div>
    
    <h3>Why RPL is a Game-Changer</h3>
    <ul>
        <li>⏱️ <strong>Time:</strong> Get qualified in weeks, not 3-4 years</li>
        <li>💰 <strong>Pay Boost:</strong> Trade workers earn 30-50% more</li>
        <li>📈 <strong>Jump:</strong> From $48/hr (assistant) to $65+/hr (tradesperson)</li>
        <li>🎫 <strong>Licences:</strong> Required for many contractor licences</li>
    </ul>
    
    <h4>How RPL Works:</h4>
    <ol style="margin-left: 20px; font-size: 11px;">
        <li><strong>Free Assessment:</strong> Initial eligibility check</li>
        <li><strong>Evidence Collection:</strong> Resume, photos, references, certificates</li>
        <li><strong>Assessment:</strong> Qualified assessor reviews against standards</li>
        <li><strong>Gap Training:</strong> Short courses if needed</li>
        <li><strong>Qualification:</strong> Receive nationally recognized Cert III</li>
    </ol>
    
    <h4>Available Through RPL:</h4>
    <table>
        <tr><th>Qualification</th><th>Experience Needed</th><th>Cost</th></tr>
        <tr><td>Cert III Fabrication (Boilermaker)</td><td>2-3 years</td><td>$2,000-$4,000</td></tr>
        <tr><td>Cert III Mechanical (Fitter)</td><td>2-3 years</td><td>$2,000-$4,000</td></tr>
        <tr><td>Cert III Carpentry</td><td>2-3 years</td><td>$1,500-$3,500</td></tr>
        <tr><td>Cert III Civil Construction</td><td>2-3 years</td><td>$1,500-$3,500</td></tr>
    </table>
    
    <div class="success-box">
        <strong>💡 Pro Tip:</strong> If you have trade experience from your home country, RPL can convert it to Australian qualifications — opening doors to much higher-paying roles immediately!
    </div>
    
    <h4>RPL Providers:</h4>
    <ul>
        <li>TAFE Queensland — tafeqld.edu.au</li>
        <li>Trade Skills Australia — tradeskillsaustralia.com.au</li>
        <li>Qualify Me! — qualifyme.edu.au</li>
        <li>Gimbal Group — gimbalgroup.com.au</li>
    </ul>
</div>

<!-- PAGE 24: TAFE COURSES -->
<div class="page">
    <h2>🎓 TAFE Courses & Earning Potential</h2>
    <p>TAFE offers practical, industry-focused training to boost your earning potential.</p>
    
    <h3>Welding Courses — High Demand</h3>
    <table>
        <tr><th>Course</th><th>Duration</th><th>Cost</th><th>Pay Boost</th></tr>
        <tr><td>Intro to Welding</td><td>3 days</td><td>~$600</td><td>Trade assistant roles</td></tr>
        <tr><td>AS1796 Certification</td><td>2-10 weeks</td><td>$1,500-$1,800</td><td>+$5-10/hr</td></tr>
        <tr><td>TIG Certification</td><td>1-3 weeks</td><td>$765</td><td>Premium TIG rates</td></tr>
        <tr><td>Cert III Fabrication</td><td>12-48 months</td><td>$3,000-$27,800</td><td>Full trade</td></tr>
    </table>
    
    <h4>AS1796 Welding Tickets:</h4>
    <table>
        <tr><th>Ticket</th><th>Process</th><th>Demand</th></tr>
        <tr><td>Ticket 1</td><td>MMA - Plate</td><td>High</td></tr>
        <tr><td>Ticket 2</td><td>MMA - Pipe</td><td>Very High</td></tr>
        <tr><td>Ticket 3E/3F</td><td>MIG/MAG</td><td>High</td></tr>
        <tr><td>Ticket 5</td><td>TIG - Light gauge</td><td>Premium</td></tr>
        <tr><td>Ticket 7</td><td>TIG - Pipe</td><td>Premium</td></tr>
    </table>
    
    <div class="success-box">
        <strong>Earning Potential:</strong>
        <ul style="margin-top: 8px; margin-bottom: 0;">
            <li>Trade Assistant (no tickets): $35-45/hr</li>
            <li>Welder with AS1796: $50-65/hr</li>
            <li>Coded Welder (mining): $65-85/hr</li>
            <li><strong>Annual difference: $30,000-$50,000+ more!</strong></li>
        </ul>
    </div>
</div>

<!-- PAGE 25: OIL & GAS -->
<div class="page">
    <h2>🛢️ Oil & Gas Offshore Pathways</h2>
    <p>Highest-paying opportunities in Australia — requires specific certifications and significant investment.</p>
    
    <div class="image-grid">
        <div>
            <img src="data:image/jpeg;base64,{oil1}" alt="Offshore oil platform">
            <p class="image-caption">Offshore oil rig operations</p>
        </div>
        <div>
            <img src="data:image/jpeg;base64,{oil2}" alt="Oil platform workers">
            <p class="image-caption">Workers on offshore platform at sunset</p>
        </div>
    </div>
    
    <h3>Is Offshore Right for You?</h3>
    <table>
        <tr><th>Factor</th><th>Consideration</th></tr>
        <tr><td>Visa Duration</td><td>Need 6+ months to make investment worthwhile</td></tr>
        <tr><td>Budget</td><td>Minimum $3,000-5,000 for certifications</td></tr>
        <tr><td>Physical Fitness</td><td>Demanding, strict medical requirements</td></tr>
        <tr><td>Commitment</td><td>2-4 weeks offshore at a time</td></tr>
    </table>
    
    <h4>Essential Offshore Tickets:</h4>
    <table>
        <tr><th>Certification</th><th>Cost</th><th>Duration</th><th>Validity</th></tr>
        <tr><td>BOSIET with CA-EBS</td><td>$2,000-$2,500</td><td>2 days</td><td>4 years</td></tr>
        <tr><td>MSIC</td><td>$100-$150</td><td>1-2 weeks</td><td>5 years</td></tr>
        <tr><td>Offshore Medical</td><td>$300-$500</td><td>Same day</td><td>2 years</td></tr>
        <tr><td>FOET (refresher)</td><td>$800-$1,200</td><td>1 day</td><td>4 years</td></tr>
    </table>
    
    <h4>Offshore Career Pathways:</h4>
    <p><strong>Entry Level:</strong></p>
    <ul>
        <li>Roustabout: General labouring — $50-65/hr</li>
        <li>Galley Hand: Catering — $40-55/hr</li>
        <li>Stores/Logistics: Inventory — $50-60/hr</li>
    </ul>
    <p><strong>Experienced:</strong></p>
    <ul>
        <li>Derrickman: Drilling operations — $65-85/hr</li>
        <li>Crane Operator: Heavy lifting — $70-90/hr</li>
        <li>Production Tech: Process ops — $70-95/hr</li>
    </ul>
    <p><strong>Senior:</strong></p>
    <ul>
        <li>Driller: Team leader — $85-120/hr</li>
        <li>OIM: Platform commander — $150,000-$300,000/year</li>
    </ul>
</div>

<!-- PAGE 26: OIL & GAS RECOMMENDATIONS -->
<div class="page">
    <h3>Recommendations by Situation</h3>
    
    <div class="info-box">
        <strong>🎯 6-12 months on visa:</strong><br>
        Start with onshore mining to build experience first. Offshore companies prefer candidates with Australian work history.
    </div>
    
    <div class="success-box">
        <strong>🎯 1-2 years remaining:</strong><br>
        Excellent time to invest. Get experience onshore (6 months), then target offshore.
    </div>
    
    <div class="warning-box">
        <strong>🎯 Tight budget:</strong><br>
        Focus on mining first — similar pay, lower entry costs. Use mining income to fund offshore tickets later.
    </div>
    
    <h4>Training Provider:</h4>
    <p><strong>ERGT Australia (Perth)</strong> — ergt.edu.au — Premier oil & gas training</p>
</div>

<!-- PAGE 27: INVESTMENT SUMMARY -->
<div class="page">
    <h2>📊 Investment Summary — Tickets & Licenses</h2>
    
    <h3>Starter Package ($500-$800)</h3>
    <p><em>For: Hospitality, Farming, Entry-level Construction</em></p>
    <table>
        <tr><th>Ticket</th><th>Cost</th><th>Opens Jobs In</th></tr>
        <tr><td>White Card</td><td>$100</td><td>All construction sites</td></tr>
        <tr><td>RSA</td><td>$80</td><td>Hospitality</td></tr>
        <tr><td>First Aid</td><td>$150</td><td>All industries</td></tr>
        <tr><td>Manual Handling</td><td>$100</td><td>All manual work</td></tr>
        <tr><td><strong>Total</strong></td><td><strong>~$430</strong></td><td></td></tr>
    </table>
    
    <h3>Construction Package ($1,500-$2,500)</h3>
    <p><em>For: Construction labouring, traffic control, warehouse</em></p>
    <table>
        <tr><th>Ticket</th><th>Cost</th></tr>
        <tr><td>White Card</td><td>$100</td></tr>
        <tr><td>Working at Heights</td><td>$300</td></tr>
        <tr><td>EWP License</td><td>$350</td></tr>
        <tr><td>Forklift License</td><td>$350</td></tr>
        <tr><td>Traffic Controller</td><td>$350</td></tr>
        <tr><td>First Aid</td><td>$150</td></tr>
        <tr><td><strong>Total</strong></td><td><strong>~$1,600</strong></td></tr>
    </table>
    
    <h3>Mining Starter Package ($3,000-$5,000)</h3>
    <p><em>For: Entry-level mining, trade assistant</em></p>
    <table>
        <tr><th>Ticket</th><th>Cost</th></tr>
        <tr><td>Standard 11 Induction</td><td>$450</td></tr>
        <tr><td>Working at Heights</td><td>$300</td></tr>
        <tr><td>Confined Space</td><td>$350</td></tr>
        <tr><td>First Aid</td><td>$150</td></tr>
        <tr><td>Manual Handling</td><td>$100</td></tr>
        <tr><td>HR License</td><td>$2,000</td></tr>
        <tr><td><strong>Total</strong></td><td><strong>~$3,350</strong></td></tr>
    </table>
</div>

<!-- PAGE 28: JOB PROGRESSION -->
<div class="page">
    <h2>📈 Job Progression Roadmap</h2>
    
    <div class="timeline">
        <div class="timeline-item">
            <div class="timeline-number">1</div>
            <div class="timeline-content">
                <strong style="color: #22c55e;">🟢 TIER 1: Hospitality ($22-$28/hr)</strong><br>
                Investment: $0-$150 | Immediate start
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-number">2</div>
            <div class="timeline-content">
                <strong style="color: #22c55e;">🟢 TIER 2: Farm Work ($28-$40/hr)</strong><br>
                Investment: $0 | Get 88 days here!
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-number">3</div>
            <div class="timeline-content">
                <strong style="color: #22c55e;">🟢 TIER 3: Construction ($35-$50/hr)</strong><br>
                Investment: $500-$2,500 | 1-3 months
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-number">4</div>
            <div class="timeline-content">
                <strong style="color: #eab308;">🟡 TIER 4: Mining Labourer ($48-$55/hr)</strong><br>
                Investment: $3,000-$5,000 | 1-3 months
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-number" style="background: #eab308;">4b</div>
            <div class="timeline-content">
                <strong style="color: #eab308;">🟡 Rigging & Scaffolding ($45-$65/hr)</strong><br>
                Investment: $4,000-$6,000 | 3-6 months experience
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-number" style="background: #a16207;">5</div>
            <div class="timeline-content">
                <strong style="color: #a16207;">🟤 Trade Qualified ($55-$80/hr)</strong><br>
                Investment: RPL $2,000-$4,000 OR Apprenticeship
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-number" style="background: #3b82f6;">6</div>
            <div class="timeline-content">
                <strong style="color: #3b82f6;">🔵 TIER 5: Mining Operator ($55-$75/hr)</strong><br>
                Investment: $6,000-$10,000 | 6-12 months experience
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-number" style="background: #1e40af;">7</div>
            <div class="timeline-content">
                <strong style="color: #1e40af;">🔵 TIER 6: Mining Senior ($70-$90+/hr)</strong><br>
                Investment: Ongoing | 2-5+ years experience<br>
                <strong>POTENTIAL: $170,000-$200,000+/year</strong>
            </div>
        </div>
    </div>
</div>

<!-- PAGE 29: FINAL ADVICE -->
<div class="page">
    <h2>💡 Final Advice</h2>
    
    <h3>Australian Work Culture</h3>
    <div class="info-box">
        <em>"Being German, I struggled with the idea of having to be perfect. Australia is different — it really is 'easy going.' Show willingness to learn, listen, and don't be arrogant."</em>
    </div>
    
    <h3>The Key to Success</h3>
    <p>Your interpersonal skills matter more than experience for lower-tier jobs. Show willingness to learn, be humble, and demonstrate reliability.</p>
    
    <h3>Avoiding Common Mistakes</h3>
    <ol style="margin-left: 20px; font-size: 11px;">
        <li>Don't get trapped in hostels — expensive accommodation drains savings</li>
        <li>Don't travel in large groups — job searching is more effective alone</li>
        <li>Don't limit yourself geographically — apply Australia-wide</li>
        <li>Don't buy the cheapest car — repairs can cost more than the vehicle</li>
        <li>Don't work cash-in-hand — no insurance, no protection</li>
        <li>Don't accept unpaid trials — it's illegal in Australia</li>
    </ol>
    
    <h3>Essential Websites</h3>
    <table>
        <tr><th>Resource</th><th>URL</th><th>Purpose</th></tr>
        <tr><td>Seek</td><td>seek.com.au</td><td>Job listings</td></tr>
        <tr><td>Indeed</td><td>au.indeed.com</td><td>Job listings</td></tr>
        <tr><td>Immigration</td><td>immi.homeaffairs.gov.au</td><td>Visa applications</td></tr>
        <tr><td>TFN Application</td><td>ato.gov.au</td><td>Tax File Number</td></tr>
        <tr><td>CITB</td><td>citb.org.au</td><td>Training subsidies</td></tr>
    </table>
    
    <div style="margin-top: 30px; text-align: center; padding: 20px; background: linear-gradient(135deg, #1e3a5f 0%, #0f172a 100%); border-radius: 12px; color: white;">
        <p style="font-size: 13px; margin-bottom: 10px;">This guide represents 13+ years of real experience. Follow the journey, learn from these mistakes, and create your own Australian success story.</p>
        <p style="font-size: 11px; color: #94a3b8;">Document Version: Professional Edition v3.0 | Last Updated: February 2026</p>
        <p style="font-size: 10px; color: #64748b;">Organization: Jobs arranged from lower-paying to higher-paying positions with clear requirements and color-coding</p>
    </div>
</div>

</body>
</html>
'''

with open('Australia_Working_Holiday_Guide_Enhanced.html', 'w') as f:
    f.write(html)

print("HTML file created successfully!")
