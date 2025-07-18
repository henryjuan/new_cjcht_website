

import os
import re

def refactor_html_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # Add viewport meta tag and Bootstrap CSS
    content = re.sub(r'(<meta http-equiv="X-UA-Compatible" content="IE=edge">)', r'\1\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">\n', content)

    # Add Bootstrap JS
    content = re.sub(r'(</body>)', r'<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>\n\1', content)

    # Replace navbar
    content = re.sub(r'<div id="logo">.*?</div><!-- end mavMenu -->', '''
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                <div class="container-fluid">
                    <a class="navbar-brand" href="/index.html"><img alt="logo" src="/user/themes/jeanlee/images/logo.png"></a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav">
                            <li class="nav-item">
                                <a class="nav-link" href="/about.html">About</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="/footwear.html">Footwear</a>
                            </li>
                            <li class="nav-item dropdown">
                                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    Culture
                                </a>
                                <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                                    <li><a class="dropdown-item" href="/culture/kehua.html">- Kehua</a></li>
                                    <li><a class="dropdown-item" href="/culture/vocalasia.html">- Vocal Asia</a></li>
                                    <li><a class="dropdown-item" href="/culture/ahouse.html">- A House</a></li>
                                    <li><a class="dropdown-item" href="/culture/boven.html">- Boven</a></li>
                                </ul>
                            </li>
                            <li class="nav-item dropdown">
                                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    Sustainability
                                </a>
                                <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                                    <li><a class="dropdown-item" href="/sustainability/net-zero-commitment.html">- Net-zero Commitment</a></li>
                                    <li><a class="dropdown-item" href="/sustainability/cdp-supplier-engagement.html">- CDP Supplier Engagement</a></li>
                                    <li><a class="dropdown-item" href="/sustainability/Environmental__Biodiversity_Public_Policy_Announcement.html">- Environmental and Biodiversity Public Policy Announcement</a></li>
                                    <li><a class="dropdown-item" href="/sustainability/Commitment_Statement_Regarding_Environmental_Position.html">- Commitment and Statement Regarding Environmental Position</a></li>
                                </ul>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="/people.html">People</a>
                            </li>
                            <li class="nav-item dropdown">
                                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    Contact
                                </a>
                                <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                                    <li><a class="dropdown-item" href="/contact/taiwan.html">- Taiwan</a></li>
                                    <li><a class="dropdown-item" href="/contact/china.html">- China</a></li>
                                    <li><a class="dropdown-item" href="/contact/others.html">- Others</a></li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
    ''', content, flags=re.DOTALL)

    # Refactor main content
    content = re.sub(r'<div id="mainContent">.*?<div  id="home-contentRight" class="im">.*?</div>.*?</div>', '''
            <div class="container">
                <div class="row">
                    <div class="col-md-8">
                        <div id="home-contentLeft">
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div id="home-contentRight" class="im">
                        </div>
                    </div>
                </div>
            </div>
    ''', content, flags=re.DOTALL)

    # Refactor footer
    content = re.sub(r'<div id="footer">.*?</div><!-- end footer -->', '''
        <footer class="container py-4 mt-5">
            <p class="text-center text-muted">© Copyright 2012 CJCHT. All Rights Reserved.</p>
        </footer>
    ''', content, flags=re.DOTALL)

    with open(file_path, 'w') as f:
        f.write(content)

if __name__ == '__main__':
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html') and file != 'index.html':
                refactor_html_file(os.path.join(root, file))

