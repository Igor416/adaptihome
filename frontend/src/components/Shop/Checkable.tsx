interface OptionProps {
  checked: boolean,
  value: string,
  onChecked: () => void,
  multiple?: boolean
}

export default function Checkable({checked, value, onChecked, multiple = false}: OptionProps) {
  return <div onClick={onChecked} className='d-flex flex-nowrap align-items-end h5 py-2'>
    <div style={{width: '2.5vh', aspectRatio: 1}} className={'bg-secondary rounded' + (multiple ? '' : '-circle')}>
      <div style={{
        transformOrigin: 'center',
        transform: `scale(${checked ? 1 : 0})`
      }} className={'bg-blue transition w-100 h-100 rounded' + (multiple ? '' : '-circle')}></div>
    </div>
    <span className='ms-2'>{value}</span>
  </div>
}