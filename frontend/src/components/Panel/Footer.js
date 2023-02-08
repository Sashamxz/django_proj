import "./Footer.css";
import { SocialIcon } from 'react-social-icons';


const Footer = () => {
  return (
    
<div className="footer">
      <div className="footer_elements">
        <SocialIcon url="https://twitter.com" />
        <SocialIcon url="https://www.facebook.com" />
        <SocialIcon url="https://www.linkedin.com" />
        <SocialIcon url="https://www.instagram.com" />
      </div>
</div>


  );
};

export default Footer;