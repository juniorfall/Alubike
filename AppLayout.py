from PIL import Image
import base64 #encode images to display format web

class AppLayout:

    def __init__(self,st):

        self.styleholder = st.empty()

    def call_markdown(self):
       
        cs = self.cssht()
        return cs

    def bytesTo64(self, bytes_file, header):
        encoded = base64.b64encode(bytes_file).decode()
        base64file = "data:%s;base64,%s" % (header, encoded)
        return base64file


    def setBackground(self, filename, filetype='image/jpeg'):
        fig = filename
        image = open(fig, 'rb').read()
        image64 = self.bytesTo64(image, filetype)
        return image64


    def cssht(self):
        
        image_center = "./image/bike.png"
        csstyle = f"""<style>

                    .reportview-container .main{{
                    background-color: #fdfefe !important;
                    }}
                    .reportview-container .main .block-container {{
                    max-width:10px;
                    
                    
                    }}
   
                    .reportview-container .main footer{{display:none;

                    }}
                  
                    .fullScreenFrame div{{
                        display: flex;
                        justify-content: center;
                    }}

                    .markdown-text-container.stMarkdown{{
                    font-size:1px;
                    }}

                    .reportview-container .markdown-text-container {{
                    position: relative;
                    text-align: justify;
                    }} 
                    
                    .main{{
                    background:url({self.setBackground(image_center, 'image/jpg')}) no-repeat top center;
                    background-size:100% auto !important;
                    position: relative;
                    flex-direction: column;
                    width: 100%;
                    overflow: auto;
                    -moz-box-align: center;
                    align-items: center;
                    }}

                    .reportview-container .css-12oz5g7 {{

                    padding: 10px !important;
                    }}

                    .reportview-container .main .block-container{{

                    max-width: 1200px;
                    }}

                    .css-d94sfw{{ display:none;

                    }}


                    button{{

                    background-color: #456fab !important;

                    }}

                    .css-1vgnld3{{color: #000000 !important;
                    font-size: 1.0em;
                    font-weight: bolder;
                    }}

                    .css-r698ls.e8zbici2{{ display:none;    

                    }}

                    
                    p{{
                    margin: 0px 0px 1rem;
                    padding: 0px;
                    font-size: 1.2rem;
                    font-weight: 600;
                    color: black;
                    }}

            
                    button:hover{{background-color: white !important;
                    color: red !important;
                    border-color: green !important;

                    }}
                    button:not(.sidebar-close):not(.control):not(.sidebar-collapse-control):not(.btn):not(.dropdown-item):not(.overlayBtn):not(.close){{
                    padding: 10px;
                    font-size: 1.0em !important;
                    color: orange;
                    border-radius: 10px;
                    box-shadow: 0 1px 4px rgba(0, 0, 0, .6);
                    }}

                    .css-ns78wr{{
                    width: 250px;
                
                    }}

                    .row-widget.stButton{{
                    width: 250px;
                    }}

                    .css-6awftf{{display: none;

                    }}

                    .css-1s0xhnp{{display: none;

                    }}

                    .element-container .stAlert{{
                    background-color: orange !important;
                    opacity: 0.75
                    }}

                    
                    .css-1d391kg{{
                    background-color: rgb(240, 242, 246);
                    background-attachment: fixed;
                    flex-shrink: 0;
                    height: 100vh;
                    overflow: auto;
                    padding: 6rem 1rem;
                    position: relative;
                    transition: margin-left 300ms ease 0s, box-shadow 300ms ease 0s;
                    width: 17rem;
                    z-index: 100;
                    margin-left: 0px;}}

                    .st-ag {{
                    font-size: 19px;
                    color: black;
                    font-weight: bolder;}}
                    
		    footer{{display: None !important;}}
                       
                    </style>"""
                    

        return csstyle
