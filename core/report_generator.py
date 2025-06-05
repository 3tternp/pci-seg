from docx import Document

def generate_report(scan_results, template_path='Issue Name Segmentation.docx', output_path='Filled_Issue_Name_Segmentation.docx'):
    # Load the DOCX template
    doc = Document(template_path)
    
    # Map scan results to template fields
    for result in scan_results:
        issue_name = result.get('issue_name', 'N/A')
        affected_ip = result.get('affected_ip', 'N/A')
        method_used = result.get('method_used', 'N/A')
        port_used = result.get('port_used', 'N/A')
        vulnerability_details = result.get('vulnerability_details', 'N/A')
        
        # Replace placeholders in the template with actual values
        for paragraph in doc.paragraphs:
            if 'Issue Name:' in paragraph.text:
                paragraph.text = f"Issue Name: {issue_name}"
            if 'Affected IP:' in paragraph.text:
                paragraph.text = f"Affected IP: {affected_ip}"
            if 'Method used:' in paragraph.text:
                paragraph.text = f"Method used: {method_used}"
            if 'Port Used:' in paragraph.text:
                paragraph.text = f"Port Used: {port_used}"
            if 'Vulnerability details:' in paragraph.text:
                paragraph.text = f"Vulnerability details: {vulnerability_details}"
    
    # Save the filled report
    doc.save(output_path)
    print(f"Report generated and saved to {output_path}")

# Example usage
if __name__ == "__main__":
    # Sample scan results
    scan_results = [
        {
            'issue_name': 'SQL Injection',
            'affected_ip': '192.168.1.1',
            'method_used': 'Automated Scan',
            'port_used': '80',
            'vulnerability_details': 'SQL Injection vulnerability found in login form.'
        },
        {
            'issue_name': 'Cross-Site Scripting (XSS)',
            'affected_ip': '192.168.1.2',
            'method_used': 'Manual Testing',
            'port_used': '443',
            'vulnerability_details': 'XSS vulnerability found in search bar.'
        }
    ]
    
    # Generate the report
    generate_report(scan_results)

from docx import Document

def generate_report(scan_results, template_path='Issue Name Segmentation.docx', output_path='Filled_Issue_Name_Segmentation.docx'):
    # Load the DOCX template
    doc = Document(template_path)
    
    # Map scan results to template fields
    for result in scan_results:
        issue_name = result.get('issue_name', 'N/A')
        affected_ip = result.get('affected_ip', 'N/A')
        method_used = result.get('method_used', 'N/A')
        port_used = result.get('port_used', 'N/A')
        vulnerability_details = result.get('vulnerability_details', 'N/A')
        
        # Replace placeholders in the template with actual values
        for paragraph in doc.paragraphs:
            if 'Issue Name:' in paragraph.text:
                paragraph.text = f"Issue Name: {issue_name}"
            if 'Affected IP:' in paragraph.text:
                paragraph.text = f"Affected IP: {affected_ip}"
            if 'Method used:' in paragraph.text:
                paragraph.text = f"Method used: {method_used}"
            if 'Port Used:' in paragraph.text:
                paragraph.text = f"Port Used: {port_used}"
            if 'Vulnerability details:' in paragraph.text:
                paragraph.text = f"Vulnerability details: {vulnerability_details}"
    
    # Save the filled report
    doc.save(output_path)
    print(f"Report generated and saved to {output_path}")

# Example usage
if __name__ == "__main__":
    # Sample scan results
    scan_results = [
        {
            'issue_name': 'SQL Injection',
            'affected_ip': '192.168.1.1',
            'method_used': 'Automated Scan',
            'port_used': '80',
            'vulnerability_details': 'SQL Injection vulnerability found in login form.'
        },
        {
            'issue_name': 'Cross-Site Scripting (XSS)',
            'affected_ip': '192.168.1.2',
            'method_used': 'Manual Testing',
            'port_used': '443',
            'vulnerability_details': 'XSS vulnerability found in search bar.'
        }
    ]
    
    # Generate the report
    generate_report(scan_results)

from docx import Document

def generate_report(scan_results, template_path='Issue Name Segmentation.docx', output_path='Filled_Issue_Name_Segmentation.docx'):
    # Load the DOCX template
    doc = Document(template_path)
    
    # Map scan results to template fields
    for result in scan_results:
        issue_name = result.get('issue_name', 'N/A')
        affected_ip = result.get('affected_ip', 'N/A')
        method_used = result.get('method_used', 'N/A')
        port_used = result.get('port_used', 'N/A')
        vulnerability_details = result.get('vulnerability_details', 'N/A')
        
        # Replace placeholders in the template with actual values
        for paragraph in doc.paragraphs:
            if 'Issue Name:' in paragraph.text:
                paragraph.text = f"Issue Name: {issue_name}"
            if 'Affected IP:' in paragraph.text:
                paragraph.text = f"Affected IP: {affected_ip}"
            if 'Method used:' in paragraph.text:
                paragraph.text = f"Method used: {method_used}"
            if 'Port Used:' in paragraph.text:
                paragraph.text = f"Port Used: {port_used}"
            if 'Vulnerability details:' in paragraph.text:
                paragraph.text = f"Vulnerability details: {vulnerability_details}"
    
    # Save the filled report
    doc.save(output_path)
    print(f"Report generated and saved to {output_path}")

# Example usage
if __name__ == "__main__":
    # Sample scan results
    scan_results = [
        {
            'issue_name': 'SQL Injection',
            'affected_ip': '192.168.1.1',
            'method_used': 'Automated Scan',
            'port_used': '80',
            'vulnerability_details': 'SQL Injection vulnerability found in login form.'
        },
        {
            'issue_name': 'Cross-Site Scripting (XSS)',
            'affected_ip': '192.168.1.2',
            'method_used': 'Manual Testing',
            'port_used': '443',
            'vulnerability_details': 'XSS vulnerability found in search bar.'
        }
    ]
    
    # Generate the report
    generate_report(scan_results)

from docx import Document

def generate_report(scan_results, template_path='Issue Name Segmentation.docx', output_path='Filled_Issue_Name_Segmentation.docx'):
    # Load the DOCX template
    doc = Document(template_path)
    
    # Map scan results to template fields
    for result in scan_results:
        issue_name = result.get('issue_name', 'N/A')
        affected_ip = result.get('affected_ip', 'N/A')
        method_used = result.get('method_used', 'N/A')
        port_used = result.get('port_used', 'N/A')
        vulnerability_details = result.get('vulnerability_details', 'N/A')
        
        # Replace placeholders in the template with actual values
        for paragraph in doc.paragraphs:
            if 'Issue Name:' in paragraph.text:
                paragraph.text = f"Issue Name: {issue_name}"
            if 'Affected IP:' in paragraph.text:
                paragraph.text = f"Affected IP: {affected_ip}"
            if 'Method used:' in paragraph.text:
                paragraph.text = f"Method used: {method_used}"
            if 'Port Used:' in paragraph.text:
                paragraph.text = f"Port Used: {port_used}"
            if 'Vulnerability details:' in paragraph.text:
                paragraph.text = f"Vulnerability details: {vulnerability_details}"
    
    # Save the filled report
    doc.save(output_path)
    print(f"Report generated and saved to {output_path}")

# Example usage
if __name__ == "__main__":
    # Sample scan results
    scan_results = [
        {
            'issue_name': 'SQL Injection',
            'affected_ip': '192.168.1.1',
            'method_used': 'Automated Scan',
            'port_used': '80',
            'vulnerability_details': 'SQL Injection vulnerability found in login form.'
        },
        {
            'issue_name': 'Cross-Site Scripting (XSS)',
            'affected_ip': '192.168.1.2',
            'method_used': 'Manual Testing',
            'port_used': '443',
            'vulnerability_details': 'XSS vulnerability found in search bar.'
        }
    ]
    
    # Generate the report
    generate_report(scan_results)

