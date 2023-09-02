import { IconDefinition } from "@fortawesome/fontawesome-svg-core";
import { faFacebookF, faInstagram } from "@fortawesome/free-brands-svg-icons";
import { faPhone } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { ResponsiveProps } from "../..";

interface ColorIcon {
  icon: IconDefinition,
  color: string
}

export default function Icons({isMobile}: ResponsiveProps) {
  const icons: ColorIcon[] = [
    {icon: faFacebookF, color: 'linear-gradient(to top, #4267B2, #4267B2)'},
    {icon: faInstagram, color: 'radial-gradient(circle at 30% 107%, #fdf497 0%, #fdf497 5%, #fd5949 45%,#d6249f 60%,#285AEB 90%)'},
    {icon: faPhone, color: 'linear-gradient(to top, #09ba26, #64fd80)'}
  ]

  return icons.map((icon, i) => 
    <div
      key={i}
      style={{width: isMobile ? '10vw' : '2vw', aspectRatio: 1, background: icon.color}}
      className='rounded-circle d-flex justify-content-center align-items-center text-white me-3'
    ><FontAwesomeIcon icon={icon.icon} /></div>
  )
}