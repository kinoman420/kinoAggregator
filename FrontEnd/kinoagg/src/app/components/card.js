import Image from 'next/image'

const Card = ({ item }) => {
    console.log(item); // Debug: Log the item data to verify
  
    if (!item) {
      return null;
    }
  
    return (
      <div className="bg-green-100  mx-6  rounded w-2/3 place-self-center justify-items-start place-items-center overflow-hidden h-12 my-10 w-100px grid grid-cols-9 text-xs">
        <div className='col-span 1  justify-self-center inline-block place-items-center w-full h-full grid  '>
            <Image
             src='/anime.png'
             width={100}
             height={100}
             alt='anime'
             className=''
             />
        </div>
        <span className="text-lg font-bold text-black text-xs col-span-4">{item.name}</span>
        
        
        <span className="text-lg font-bold text-black whitespace-nowrap text-xs col-span-1 justify-self-center">
          
          <a href={item.link} target="_blank" rel="noopener noreferrer">
            Magnet Link
          </a>
        </span>
        <span className="text-lg font-bold text-black whitespace-nowrap text-xs col-span-1 justify-self-center"> {item.size}</span>
        <span className="text-lg font-bold text-black whitespace-nowrap text-xs text-green-400 col-span-1 justify-self-center"> {item.seeds}</span>
        <span className="text-lg font-bold text-black whitespace-nowrap text-xs text-red-600 col-span-1 justify-self-center"> {item.leech}</span>
      </div>
    );
  };
  
  export default Card;
  