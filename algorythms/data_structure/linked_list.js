class LinkedListNode {
    constructor(value, next){
        this.value=value
        this.next=next
    }
}

const head = new LinkedListNode(5,
    new LinkedListNode(8,
        new LinkedListNode(12,
            new LinkedListNode(3, null)
        )
    )
)

class LinkedList {
    head = null

    add(value){
        this.head = new LinkedListNode(value, this.head)
    }

    insert(index, value){
        if(this.head === null)
            this.head = new LinkedListNode(value, null)
        else if(index === 0)
            this.add(value)
        else{
            let current = this.head
            while (current.next !== null && index > 1){
                current = current.next
                index -= 1
            }
            current.next = new LinkedListNode(value, current.next)
        }
    }

    contain(value){
        let current = this.head;

        while(current !== null){
            if(current.value === value){
                return true;
            }
            current = current.next;
        }
        return false;
    }

    len() {
        let result=0;
        let current=this.head;

        while (current !== null){
            result+=1;
            current=current.next;
        }

        return result;
    }

    remove(){
        if(this.head===null){
            return undefined;
        }

        const value=this.head.value;

        this.head=this.head.next;

        return value;
    }

    removeAt(index){
        if(this.head===null){
            return undefined;
        }
        else if(index===0||this.head.next===null){
            return this.remove()
        }
        else{
            let current=this.head;
            while(current.next.next!==null && index>1){
                current=current.next;
                index-=1;
            }
            const value=current.next.value;
            current.next=current.next.next;

            return value;
        }
    }
}
