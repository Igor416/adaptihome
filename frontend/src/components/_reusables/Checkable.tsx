import { ReactNode } from "react"

interface OptionProps {
  checked: boolean,
  value: ReactNode,
  onChecked: () => void,
  multiple?: boolean
}

export default function Checkable({checked, value, onChecked, multiple = false}: OptionProps) {
  return <div onClick={onChecked} className='d-flex flex-nowrap align-items-end h5 py-3'>
    <div style={{width: '2.5vh', aspectRatio: 1}} className={'bg-secondary rounded' + (multiple ? '' : '-circle')}>
      <div style={{
        transformOrigin: 'center',
        transform: `scale(${checked ? 1 : 0})`
      }} className={'bg-blue transition w-100 h-100 rounded' + (multiple ? '' : '-circle')}></div>
    </div>
    <span className='ms-2 flex-grow-1'>{value}</span>
  </div>
}