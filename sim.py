import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('dark_background')
from matplotlib.animation import FuncAnimation as animation


inf_col = 'red'
rec_col = 'lime'
suc_col = 'grey'

infection_radius = 0.6
recovery_rate = 0.01
stage_dimension = 20 # MxM square stage

init = [100, # pop. size
        2, # infected
        0] #removed

class Sim():
    def __init__(self,init):
        #init = [N,inf,rec]
        self.N = init[0]
        suc = self.N-init[1]-init[2]
        self.cols = np.repeat([suc_col,inf_col,rec_col],
                              [suc,init[1],init[2]])
        self.low,self.high = -stage_dimension/2,stage_dimension/2
        self.pos = np.random.uniform(self.low,self.high,size=(2,self.N))
        
        self.stream = self.data_stream()
        self.fig,self.ax = plt.subplots();
        
        self.ani = animation(self.fig, self.update, interval=80, 
                                          init_func=self.setup, blit=True)

    def setup(self):
        p,c= next(self.stream)
        
        self.scat = self.ax.scatter(x=p[0,:],
                                    y=p[1,:],
                                    c=c.T)
        return self.scat,
    
    def arg_within_radius(self,inf,succeptible,r):
        #inf 1x2, succeptible nx2 matrices
        dist = np.sqrt(((inf-succeptible)**2).sum(axis=1))
        return np.argwhere(dist<r).ravel()
    
    def data_stream(self):
        while True:
            #move points
            jitter = 0.1*np.random.normal(0,1,size=(2,self.N))
            self.pos[0:2,:]+=jitter

            #infect and recover---------
            #get infected people
            inf = np.argwhere(self.cols == inf_col).ravel()
            inf_people = self.pos[:,inf].T

            for i in inf_people:
                suc = np.argwhere(self.cols == suc_col).ravel()
                suc_people = self.pos[:,suc].T

                infect = self.arg_within_radius(i,suc_people,infection_radius)
                infect_index = suc[infect]
                self.cols[infect_index] = inf_col
            
            #adjust out of bounds
            x1=np.where(self.pos[0:2,:]<self.low)
            x2=np.where(self.pos[0:2,:]>self.high)
            self.pos[0:2,:][x1],self.pos[0:2,:][x2] = self.low,self.high
            
            #yield [self.pos,self.cols],
            r = np.random.uniform(0,1, size = inf.size)
            rec = np.argwhere(r<recovery_rate).T
            recovered_idx = inf[rec]
            self.cols[recovered_idx] = rec_col
            
            yield self.pos,self.cols
            
    def update(self,i):
        data,c= next(self.stream)
        self.scat.set_offsets(data[0:2,:].T)
        self.scat.set_sizes(np.zeros(self.N)+10)
        self.scat.set_color(c.T)
        return self.scat,



def main():
    S = Sim(init)
    plt.show()

if __name__ == "__main__":
    main()
