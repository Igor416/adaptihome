import { ResponsiveProps } from "../.."

interface SideTextProps extends ResponsiveProps {
  text: string,
  right: string
}

export default function SideText({text, right, isMobile}: SideTextProps) {
  if (isMobile) {
    return <div></div>
  }
  return <div
    style={{
      top: '80vh', 
      right: `-${right}vw`,
      transform: 'rotate(-90deg)'
    }}
    className='position-absolute overflow-hidden'
  >
    <span
      style={{
        opacity: 0.2,
        fontSize: '15vw',
        transform: 'translateY(5vw)'
      }}
      className='d-block text-blue overflow-hidden'
    >{text}</span>
  </div>
}